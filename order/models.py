from django.db import models


class PointOfIssue(models.Model):
    title = models.CharField(verbose_name='Адрес пункта выдачи', max_length=255, unique=True)

    class Meta:
        verbose_name = 'Адрес пункта выдачи'
        verbose_name_plural = 'Адреса пункта выдачи'

    def __str__(self) -> str:
        return self.title


class Order(models.Model):
    product_name = models.CharField(verbose_name='Название продукта', max_length=255)
    product_type = models.CharField(verbose_name='Тип продукта', max_length=255)
    delivery_date = models.DateField(verbose_name='Дата доставки')
    addresses = models.ManyToManyField(PointOfIssue, verbose_name='Адреса пункта выдачи')
    addresses_file = models.FileField(blank=True, null=True, verbose_name='Файл с адресами')
    create_at = models.DateTimeField(verbose_name='Время заказа', auto_now_add=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    
