# def add(*args):
#     sum = 0
#     for num in args:
#         sum += num
#     return sum
#
# print(add(1, 2, 3, 4, 56, 77))
#
# # def calculate(n, **kwargs):
# #     # for key, value in kwargs.items():
# #     #     print(key, value)
# #     n += kwargs["add"]
# #     n *= kwargs["multiply"]
# #     print(n)
# #
# #
# # calculate(2, add=3, multiply=5)
# #
# # class Car:
# #
# #     def __init__(self, **kwargs):
# #         self.make = kwargs.get("make")
# #         self.model = kwargs.get("model")
# #         self.year = kwargs.get("year")
# #         self.price = kwargs.get("price")
# #
# # my_car = Car(make="BMW", model="M2CS", year=2025)
# # print(my_car.price)
#
# def test(*args):
#     print(args)
#
# test(1, 2, 3, 5)
# type(test())

def all_aboard(a, *args, **kwargs):
    print(a, args, kwargs)

all_aboard(4, 7, 3, 0, x=10, y=64)