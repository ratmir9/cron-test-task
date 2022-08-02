from django.db import models


class TypeProduct(models.Model):
    title = models.CharField(verbose_name='Название типа товара', max_length=255, unique=True)

    class Meta:
        verbose_name = 'Тип товара'
        verbose_name_plural = 'Типы товара'

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255, unique=True)
    type = models.ForeignKey(TypeProduct, verbose_name='Тип товара', on_delete=models.CASCADE)
    create_at = models.DateTimeField(verbose_name='Время добавления', auto_now_add=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self) -> str:
        return self.title
    
