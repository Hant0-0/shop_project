from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart(object):
    # Ініціалізуємо корзину
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CARD_SESSION_ID)
        if not cart:
            # Зберігаємо пустру карту в сесії
            cart = self.session[settings.CARD_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        # Додати продукт до корзини або обновити його кількість
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Оновлення сесії cart
        self.session[settings.CARD_SESSION_ID] = self.cart
        # Відмітити сеанс як змінений, що побачити що він збережений
        self.session.modified = True

    def remove(self, product):
        # Видалення товару з корзини
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()

    def __iter__(self):
        # Перебір елементів з корзини і отримання продуктів з бази даних
        self.products_ids = self.cart.keys()

        # Отримуєм об'єкт product і розміщуєм його в корзину
        products = Product.objects.filter(id__in=self.products_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        # Підрахунок кількості товарів
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        # Підрахунок ціни товарів у корзині
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # видалення корзини із сеансу
        del self.session[settings.CARD_SESSION_ID]
        self.session.modified = True
