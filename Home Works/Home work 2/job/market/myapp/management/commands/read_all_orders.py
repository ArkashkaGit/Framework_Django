from django.core.management.base import BaseCommand
from myapp.models import Order


class Command(BaseCommand):
    help = 'Выбрать заказ для просмотра заказа, указав ID заказа передав один аргумент'

    def handle(self, *args, **kwargs):
        order = Order.objects.all()
        print(order)