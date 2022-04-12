from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    f_name = models.CharField(max_length=200, null=True, blank=True)
    l_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return f' {self.f_name} {self.l_name}'


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return f'{self.name} : {self.price} €'


class Status(models.Model):

    SHOPPING_STATUS = (
        ('A', "Order accepted"),
        ('C', "Carried out"),
        ('F', "Order finished"),
    )

    status = models.CharField(
        max_length=1,
        choices=SHOPPING_STATUS,
        blank=True,
        default='A',
        help_text="Status",
    )

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status"

    def __str__(self):
        return f'{self.status}'


class Order(models.Model):
    customer_id = models.ForeignKey('Customer', related_name="customer", on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateField("Ordered date", null=True, blank=True)
    status_id = models.ForeignKey("Status", on_delete=models.SET_NULL, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.productorder_set.all()
        total = sum([item.get_total_amount for item in orderitems])
        return total

    @property
    def get_all_items(self):
        orderitems = self.productorder_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class ProductOrder(models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.SET_NULL, blank=True, null=True)
    order_id = models.ForeignKey('Order', on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        verbose_name = "Product Order"
        verbose_name_plural = "Product Orders"

    def __str__(self):
        return f'{self.product_id}'

    @property
    def get_total_amount(self):
        total = self.product_id.price * self.quantity
        return total