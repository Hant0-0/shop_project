from django.db import models
from shop.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=120)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    city = models.CharField(max_length=150)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-create',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_price(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name='order', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='order_item', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_cost(self):
        return self.quantity * self.price

    def __str__(self):
        return '{}'.format(self.id)
