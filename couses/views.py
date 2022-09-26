from django.core.paginator import Paginator
from django.http import request, JsonResponse
from blogs.models import Blog
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from . models import *
from paytm import Checksum
import requests
from django .conf import settings
from django.views.decorators.csrf import csrf_exempt
from paymentintigration.views import getPaytmParam, getRozorpayClient,verifyPaymentRequest,PaypalParam,verifyPayPalPayment
# Create your views here.
def ConvertCurrency(currency,Ccod,convTo):
    try:
        conQry = f"{Ccod}_{convTo}"
        url = f"https://free.currconv.com/api/v7/convert?q={conQry}&compact=ultra&apiKey=afcd25a222160e9a3bcb"
        data = requests.get(url)
        js = data.json()[conQry]
        covAmount = float(js)*float(currency)
        return covAmount
    except Exception as e:
        return None
def couses(request,slug=None,cat=None):
    res= {}
    if slug is not None:
        #for single couse
        res['couse'] = Couses.objects.get(slug = slug)
        return render(request,'couses/single-couse.html',res)
    # for couse list
    res['couseslist'] = Couses.objects.all().order_by('-time')
    res['title'] = "Our Couses"
    if cat is not None:
        res['couseslist'] = res['couseslist'].filter(category__slug=cat)
        res['title'] = Category.objects.get(slug=cat).name
    paginator = Paginator(res['couseslist'], 5) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    res['page_obj'] = paginator.get_page(page_number)
    res['categories'] = Category.objects.all().order_by('name')
    return render(request,'couses/couses.html',res)

def genrateOrder(request, slug,orderid=None):
    fname=request.POST['fname']
    lname=request.POST['lname']
    email=request.POST['email']
    currency=request.POST['currency_code']
    # ammount=float(request.POST['selamount'])
    ammount = request.POST['amount']
    # cammount = ConvertCurrency(ammount,currency,"USD")
    cammount = None
    ammount = cammount if cammount is not None else ammount
    couseob = Couses.objects.get(slug=slug)
    Donation = donation.objects.create(first_name = fname, last_name = lname,  email= email , ammount = ammount,  couse = couseob , currency=currency,transactionid = 'NO transaction')
    if orderid is not None:
        Donation.order_id = orderid
    Donation.save()
    return Donation

def paymenthandler(request,slug=None):
    if request.method=="POST":
        mode = request.POST['paymentmode']
        if mode == 'paypal':
            return paypalHandler(request,slug)
        if mode == 'paytm':
            return paytmHandler(request,slug)
        if mode == 'rozorpay':
            return rozorpayHandler(request,slug)

    # items = charityblog.objects.get(id = num)
    # pers = str((float(items.blog_raised)*100)/float(items.blog_goal))[:4]
    # return render(request , 'donation/payment.html',{'blog':items,'per':pers})

def paytmHandler(request,slug=None):
    if request.method=="POST":
        Donation = genrateOrder(request,slug)
        param_dict,renderhtml =  getPaytmParam(request,Donation.order_id,Donation.ammount,Donation.email,'handle',Donation.currency)
        print(param_dict)
        return renderhtml




@csrf_exempt
def hendlerequest(request):
    if request.method =='POST':
        # form = request.POST
        # response_dict= {}
        # for i in form.keys():
        #     response_dict[i]=form[i]
        #     if i == 'CHECKSUMHASH':
        #         checksum = form[i]
        # print(response_dict)
        # MERCHANT_KEY = 'a1Q7vq@5Q#PvFVc@'
        # verify = Checksum.verify_checksum(response_dict,MERCHANT_KEY,checksum)
        verify,response_dict = verifyPaymentRequest(request)
        if verify:
            if response_dict['RESPCODE'] == '01':
                donationblog = donation.objects.get(order_id = response_dict['ORDERID'])
                if donationblog.transactionid == 'NO transaction':
                    Blog = Couses.objects.get(id = donationblog.couse.id)
                    Blog.raised = float(Blog.raised) + float(response_dict['TXNAMOUNT'])
                    Blog.save()
                response_dict['couse'] = float(response_dict['TXNAMOUNT'])
                donationblog.transactionid = response_dict['TXNID']
                donationblog.save()
            else:
                try:
                    Donation=donation.objects.get(order_id=int(response_dict['ORDERID']))
                    Donation.delete()
                except Exception as e:
                    pass
        else:
            print("order unsuccessful because",response_dict['RESPMSG'])
        return render(request,'couses/paymentstatus.html',{'response': response_dict})
def paypalHandler(request,slug):
     if request.method=="POST":
        Donation = genrateOrder(request,slug)
        request.session["orderid"] =  Donation.order_id
        paypal_dict ,form  = PaypalParam(request,Donation.order_id,Donation.email,Donation.ammount,Donation.currency)
        return render(request, 'couses/process_payment.html', {'order': Donation, 'form': form})
@csrf_exempt
def payment_done(request):
    try:
        response = verifyPayPalPayment(request.session["orderid"])
        return render(request, 'couses/payment_done.html',{'response':response})
    except Exception as e:
        response = donation.objects.get(order_id =  request.session['orderid']).__dict__
        return render(request, 'couses/payment_done.html',{'response':response})
def getpaypalPaymentStatus(request):
    try:
        response = verifyPayPalPayment(request.session["orderid"])
        return JsonResponse(response,status=200)
    except Exception as e:
        return JsonResponse({},status=404)
 

@csrf_exempt
def payment_canceled(request):
    return render(request, 'couses/payment_cancelled.html',{})


from django.urls import reverse
def rozorpayHandler(request,slug):
    Donation = genrateOrder(request,slug) 
    amount = int(float(Donation.ammount)*100)
    print(amount)
    currency = Donation.currency
    # Create a Razorpay Order
    razorpay_client,config = getRozorpayClient()
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    Donation.order_id = razorpay_order_id
    Donation.save()
    callback_url = reverse('rozorpayhanle')
 
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = config.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
 
    return render(request, 'couses/rozorpay.html', context=context)



@csrf_exempt
def rozorhandler(request):
    if request.method == "POST":
        print(request.POST)
            # get the required parameters from post request.
        payment_id = request.POST.get('razorpay_payment_id', '')
        razorpay_order_id = request.POST.get('razorpay_order_id', '')
        signature = request.POST.get('razorpay_signature', '')
        Donation = donation.objects.get(order_id = razorpay_order_id)
        params_dict = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        }

        # verify the payment signature.
        razorpay_client,config = getRozorpayClient()
        result = razorpay_client.utility.verify_payment_signature(
            params_dict)
        if result is None:
            amount = int(float(Donation.ammount)*100) # Rs. 200
                # capture the payemt
            razorpay_client.payment.capture(payment_id, amount)
            if Donation.transactionid == 'NO transaction':
                Blog = Couses.objects.get(id = Donation.couse.id)
                Blog.raised = float(Blog.raised) + float(Donation.ammount)
                Donation.transactionid = payment_id,
                Donation.save()
                Blog.save()
            # render success page on successful caputre of payment
            return render(request, 'couses/paymentsuccess.html',{"response":Donation})
        else:

            # if signature verification fails.
            return render(request, 'couses/paymentfail.html',{"response":Donation})
