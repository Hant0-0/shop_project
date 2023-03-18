from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(db_index=True)

    class Meta:
        ordering = ['name', ]
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.name




class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(db_index=True)
    description = models.TextField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(blank=True)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField(max_length=20)
    update = models.DateTimeField(auto_now_add=True)
    date_create = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name', ]
        index_together = ['id', 'slug']

    def __str__(self):
        return self.name

