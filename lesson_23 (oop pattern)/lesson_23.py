# S - (S...) принцип единства ответственности
# O - (OCP - The open-closed principle) принцип открытости-закрытости
# L - (LSP - The Liskov Substitution Principle) принцип подстановки Лисков
# I - (ISP) принцип разделения интерфейсов
# D - (DIP - The Dependency Inversion Principle) принцип


# Tests
# import unittest
# from fractions import Fraction
#
#
# class FractionCalculator:
#     def __init__(self, numerator, denominator):
#         self.fraction = Fraction(numerator, denominator)
#
#     def add(self, other):
#         return self.fraction + other.fraction
#
#     def sub(self, other):
#         return self.fraction - other.fraction
#
#     def mult(self, other):
#         return self.fraction * other.fraction
#
#     def div(self, other):
#         return self.fraction // other.fraction
#
#
# class TestFractionCalculator(unittest.TestCase):
#     def setUp(self):
#         self.frac1 = FractionCalculator(1, 2)
#         self.frac2 = FractionCalculator(1, 4)
#
#     def test_add(self):
#         self.assertEqual(self.frac1.add(self.frac2), Fraction(3, 4))
#
#     def test_sub(self):
#         self.assertEqual(self.frac1.sub(self.frac2), Fraction(1, 4))
#
#     def test_mult(self):
#         self.assertEqual(self.frac1.mult(self.frac2), Fraction(1, 8))
#
#     def test_div(self):
#         self.assertEqual(self.frac1.div(self.frac2), Fraction(2, 1))
#
#
# if __name__ == '__main__':
#     unittest.main()


import unittest


class Calculator:
    def __init__(self, num):
        self.num = num

    def add(self, other):
        return self.num + other.num

    def sub(self, other):
        return self.num - other.num

    def mult(self, other):
        return self.num * other.num

    def div(self, other):
        return self.num // other.num

    def max(self, other):
        return max(self.num, other.num)

    def min(self, other):
        return min(self.num, other.num)

    def percent(self, other):
        return self.num / 100 * other.num

    def degree(self, other):
        return self.num ** other.num


class TestCalculator(unittest.TestCase):

    def setUp(self) -> None:
        self.num1 = Calculator(10)
        self.num2 = Calculator(5)

    def test_add(self):
        self.assertEqual(self.num1.add(self.num2), 15)

    def test_sub(self):
        self.assertEqual(self.num1.sub(self.num2), 5)

    def test_mult(self):
        self.assertEqual(self.num1.mult(self.num2), 50)

    def test_div(self):
        self.assertEqual(self.num1.div(self.num2), 2)

    def test_max(self):
        self.assertEqual(self.num1.max(self.num2), 10)

    def test_min(self):
        self.assertEqual(self.num1.min(self.num2), 5)

    def test_percent(self):
        self.assertEqual(self.num1.percent(self.num2), 0.5)

    def test_degree(self):
        self.assertEqual(self.num1.degree(self.num2), 100000)
