from dataclasses import fields
from django import forms
from order.models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'delivery_date', 'point_of_issue']

    

