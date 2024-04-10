import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_project.settings')

app = Celery('shop_project')
app.config_from_object('django.conf.settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule ={
    'every': {
        'task': 'catalog.task.some_scheduled_task',
        'schedule': 10
    },
    'client_orders':{
        'task': 'catalog.task.check_order_and_send_mails',
        'schedule': crontab(minute="*/1")
    }
}
