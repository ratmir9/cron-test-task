import os
from django.conf import settings

from base_services import generate_file_name
from order.models import Order


class OrderService:
    order_query = Order.objects.select_related('product__type')

    def get_order_by_order_id(self, order_id):
        try:
            return self.order_query.get(id=order_id)
        except Order.DoesNotExist:
            return ''

    def get_all_orders(self):
        return self.order_query.all()

    def write_file_addresses(self, addresses):
        file_name = generate_file_name()
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
        with open(f'{file_path}.txt', 'w') as file:
            for address in addresses:
                file.write(address.title + '\n')
        return file_name + '.txt'

    def add_point_of_issue(self, order, addresses):
        for address in addresses:
            order.point_of_issue.add(address)
            order.save()
        return order 

    def add_order(self, order_data):
        addresses = order_data.pop('point_of_issue') 
        order = Order.objects.create(**order_data)
        return self.add_point_of_issue(order, addresses)
        