from django import forms
from order.models import  Order, PointOfIssue


class PointOfIssueForn(forms.ModelForm):
    title = forms.CharField(label='Адрес пункта выдачи', max_length=255)
    class Meta:
        model = PointOfIssue
        exclude = ['title']


PointOfIssueFornset = forms.formset_factory(PointOfIssueForn, extra=2)

class OrderCreateForm(forms.ModelForm):
    addresses = PointOfIssueFornset()
    class Meta:
        model = Order
        fields = ['product_name', 'product_type', 'delivery_date', 'addresses_file']


    

