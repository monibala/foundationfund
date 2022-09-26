from django.shortcuts import get_object_or_404
from .models import donation,Couses
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver


@receiver(valid_ipn_received)
def payment_notification(sender, **kwargs):
    ipn = sender
    if ipn.payment_status == 'Completed':
        # payment was successful
        order = get_object_or_404(donation, order_id=ipn.invoice)
        if order.transactionid == 'NO transaction':
            # mark the order as paid
            order.transactionid = ipn.txn_id
            order.save()
            Blog = Couses.objects.get(id = order.couse.id)
            Blog.raised = float(Blog.raised) + float(order.ammount)
            Blog.save()