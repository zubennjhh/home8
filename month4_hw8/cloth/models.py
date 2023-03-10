from django.db import models


class CustomerCL(models.Model):
    name = models.CharField('Имя клиента', max_length=50)
    surname = models.CharField('Фамилия клиента', max_length=50)
    address = models.CharField('Адрес', max_length=100)
    phone = models.CharField('Номер телефона', max_length=25)
    email = models.EmailField('Почта')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TagCL(models.Model):
    name = models.CharField('Наименование тега', max_length=50)

    def __str__(self):
        return self.name


class ProductCL(models.Model):
    class Meta:
        verbose_name = "Одежда"
        verbose_name_plural = "Одежда"

    name = models.CharField('Название одежды', max_length=50)
    image = models.ImageField('Картинка', upload_to='', null=True)
    price = models.PositiveIntegerField('Цена')
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(TagCL)

    def __str__(self):
        return self.name


class OrderCL(models.Model):
    STATUS = (
        ("На обработке", "На обработке"),
        ("В пути", "В пути"),
        ("Доставлен", "Доставлен"),
    )
    customer = models.ForeignKey(CustomerCL, on_delete=models.CASCADE)
    product = models.ForeignKey(
        ProductCL, on_delete=models.CASCADE, related_name="order_product"
    )
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS)

    def __str__(self):
        return self.product.name
