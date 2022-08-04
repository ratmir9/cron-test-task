from order.models import Order


class OrderService:
    def get_order_by_order_id(self, order_id):
        try:
            return Order.objects.prefetch_related('addresses').get(id=order_id)
        except Order.DoesNotExist:
            return ''

    def get_all_orders(self):
        return Order.objects.all()

    def create_order(self, order_data):
        return Order.objects.create(**order_data)

        