from celery import shared_task
import time
from catalog.models import Order
from datetime import timedelta
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def some_task():
    time.sleep(5)
    return 'Aboba'

@shared_task
def some_scheduled_task():
    return 'DAROVA'


@shared_task
def check_order_and_send_mails():
    orders = Order.objects.filter(payment_status='Paid')

    for order in orders:
        if not order.if_notif_sent:
            send_mail(
                'Order from Aboba-shop',
                f'Your order {order.id} is on the way!',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[order.user.email],
            )

            order.if_notif_sent = True
            order.save()