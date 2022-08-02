from django.contrib import admin

from order.models import PointOfIssue, Order


admin.site.register(PointOfIssue)
admin.site.register(Order)
