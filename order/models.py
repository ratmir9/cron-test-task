from django.db import models

from product.models import Product

class PointOfIssue(models.Model):
    title = models.CharField(verbose_name='Адрес пункта выдачи', max_length=255, unique=True)

    class Meta:
        verbose_name = 'Адрес пункта выдачи'
        verbose_name_plural = 'Адреса пункта выдачи'

    def __str__(self) -> str:
        return self.title


class Order(models.Model):
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    delivery_date = models.DateField(verbose_name='Дата доставки')
    point_of_issue = models.ManyToManyField(PointOfIssue, verbose_name='Пункт выдачи')
    issuing_addresses_file = models.FileField(upload_to='media')
    create_at = models.DateTimeField(verbose_name='Время заказа', auto_now_add=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

        





