from django.urls import reverse
from django.http import  HttpResponseRedirect, Http404
from django.views.generic import ListView, CreateView, DetailView
# from django.views.generic.detail import DetailView
from order.models import Order
from order.services.order_services import OrderService
from order.forms import OrderCreateForm, PointOfIssueFornset
from order.logic import OrderLogic    

class OrderCreate(CreateView):
    form_class = OrderCreateForm
    template_name = 'add_order.html'
    order_logic = OrderLogic()

    def get_context_data(self, **kwargs):
        data = super(OrderCreate, self).get_context_data(**kwargs)
        if self.request.method == 'POST':
            data['form'] = OrderCreateForm(self.request.POST, self.request.FILES)
            data['addresses'] = PointOfIssueFornset(self.request.POST)
        else:
            data['addresses'] = PointOfIssueFornset()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        addresses = context['addresses']
        if addresses.is_valid():
            self.order_logic.create_order(
                order_data=form.cleaned_data,
                point_of_issue_data=addresses.cleaned_data
            )
        return HttpResponseRedirect(reverse('orders'))


class OrderView(ListView):
    model = Order
    template_name = 'orders.html'
    order_service = OrderService()

    def get_queryset(self):
        return self.order_service.get_all_orders()


class OrderDetailView(DetailView):
    model = Order
    template_name = 'detail_order.html'
    pk_url_kwarg = 'order_id'
    order_service = OrderService()
    
    def get_object(self, queryset=None):
        order = self.order_service.get_order_by_order_id(order_id=self.kwargs['order_id'])
        if not order:
            raise Http404(f'order with not found')
        return order
