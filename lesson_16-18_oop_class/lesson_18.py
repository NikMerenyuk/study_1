# class MyZeroDivisionError(ZeroDivisionError):
#     def __init__(self, message=''):
#         self.message = message
#
#
# def division(a, b):
#     try:
#         if b == 0:
#             raise MyZeroDivisionError('Деление на ноль')
#     except MyZeroDivisionError as error:
#         return error
#
#
# print(division(3, 0))


# class Vehicle:
#
#     def __init__(self, weight):
#         self.weight = weight
#
#
# class Ship(Vehicle):
#     pass
#
#
# base_vehicle = Vehicle(100)
# ship = Ship(100)

# print(isinstance(base_vehicle, Vehicle))    # Проверяет
# print(isinstance(ship, Vehicle))
# print(issubclass(Ship, Vehicle))    # Проверяет относится ли класс Ship к классу Vehicle


# class Multiply:
#     def __init__(self, num_1, num_2):
#         self.num_1 = num_1
#         self.num_2 = num_2
#
#     def __call__(self, *args, **kwargs):
#         print(f'Hi {kwargs["name"]}')
#         return self.num_1 * self.num_2
#
#
# multiply = Multiply(10, 15)
# result = multiply(name='Smith')
# print(result)


# Перегрузка операторов

class Number:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self.number + other.number)
        else:
            return 'Сложение невозможно!'

    def __sub__(self, other):
        if isinstance(other, Number):
            return Number(self.number - other.number)
        else:
            return 'Вычитание невозможно!'

    def __mul__(self, other):
        if isinstance(other, Number):
            return Number(self.number * other.number)
        else:
            return 'Вычитание невозможно!'

    def __truediv__(self, other):
        if isinstance(other, Number):
            return Number(self.number / other.number)
        else:
            return 'Деление невозможно!'

    def __eq__(self, other):
        if isinstance(other, Number):
            return self.number == other.number
        else:
            return 'Сравнение невозможно'

    def __ne__(self, other):
        if isinstance(other, Number):
            return self.number != other.number
        else:
            return 'Сравнение невозможно'


number_1 = Number(10)
number_2 = Number(1)
number_3 = Number(12)
# result = (number_1 / number_2) * number_3
# print(result.number)
print(number_1 > number_2)


# КОРЗИНА
#
class Product:

    def __init__(self, name, price, quantity, shop, discount=0.5):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.shop = shop
        self.discount = discount

    def get_total_product_price(self):
        return (self.price - self.price * self.discount) * self.quantity


class Shop:

    def __init__(self, name):
        self.name = name


class Cart:

    def __init__(self):
        self.cart = []

    def __add__(self, other):
        if isinstance(other, Cart):
            # merge_cart = Cart()
            # merge_cart.cart = self.cart + other.cart
            # return merge_cart

            self.cart += other.cart
            return self
        return 'Невозможно произвести слияние корзин!'

    def add_product(self, *args):
        for i_product in args:
            self.cart.append(i_product)

    def get_all_products_in_cart(self):
        print('Товары в корзине:')
        for i_product in self.cart:
            print(f'Название: {i_product.name}; Цена: {i_product.price}; '
                  f'Кол-во: {i_product.quantity}; '
                  f'Общая стоимость: {i_product.get_total_product_price()}; '
                  f'Магазин: {i_product.shop.name}')
        print(f'Общая стоимость товаров в корзине: {self.get_total_cart_amount()}')

    def get_total_cart_amount(self):
        total_price = sum([i_product.get_total_product_price()
                           for i_product in self.cart])
        return total_price


shop_1 = Shop('Magnit')
shop_2 = Shop('Monetka')

cart_1 = Cart()
cart_1.add_product(Product('apple', 100, 5, shop_1, 0.5), Product('Fish', 500, 2, shop_1))
cart_1.get_all_products_in_cart()

cart_2 = Cart()
cart_2.add_product(Product('banana', 100, 3, shop_2), Product('snake', 1500, 2, shop_2))
cart_2.get_all_products_in_cart()

# cart_3 = cart_1 + cart_2
# cart_3.get_all_products_in_cart()

cart_1 += cart_2
cart_1.get_all_products_in_cart()
del cart_2


