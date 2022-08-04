from django.urls import path
from order.views import (
     OrderCreate,
     OrderDetailView,  
     OrderView
)


urlpatterns = [
     path('add/', OrderCreate.as_view(), name='add_order'),
     path('<int:order_id>/', OrderDetailView.as_view(), name='detail_order'),
     path('', OrderView.as_view(), name='orders')
]
