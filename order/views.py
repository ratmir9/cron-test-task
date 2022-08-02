from django.urls import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views import View

from order.services import OrderService
from order.forms import OrderCreateForm


class OrderCreateView(View):
    order_service  = OrderService()

    def get(self, request):
        order_create_form = OrderCreateForm()
        context = {'form': order_create_form}
        return render(request, 'add_order.html', context)

    def post(self, request):
        order_create_form = OrderCreateForm(request.POST)
        if order_create_form.is_valid():
            data = order_create_form.cleaned_data
            file_name = self.order_service.write_file_addresses(
                addresses=data['point_of_issue']
            )
            data['issuing_addresses_file'] = file_name
            self.order_service.add_order(data)
            return HttpResponseRedirect(reverse('orders'))
        return render(request, 'add_order.html', {'form': order_create_form})


class OrderView(View):
    order_service = OrderService()
    
    def get(self, request):
        orders = self.order_service.get_all_orders()
        return render(request, 'orders.html', {'orders': orders})    


class OrderDetailView(View):
    order_service = OrderService()
    def get(self, request, order_id):
        order = self.order_service.get_order_by_order_id(order_id)
        if not order:
            raise Http404('Такаого заказа нет')
        return render(request, 'detail_order.html', {'order': order})
