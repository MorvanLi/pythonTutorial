# -*- coding: utf-8 -*-
# @Time    : 2022/7/24 0:59
# @Author  : Li Bo
# @FileName: 724.py
# @Software: PyCharm

from collections import Iterable


# class MyIterator:
#     """
#     define my iterator
#     """
#
#     def __init__(self, num1: int = 0, num2: int = 1, max_iter: int = 10):
#         self.num1 = num1
#         self.num2 = num2
#         self.max_iter = max_iter
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.max_iter -= 1
#         if self.max_iter > 0:
#             self.num1, self.num2 = self.num2, self.num1 + self.num2
#             return self.num2
#         else:
#             raise StopIteration
#
#
# mi = MyIterator()
# print(next(mi))
# print(next(mi))
# print(next(mi))
# print(next(mi))
# print(next(mi))
# print(next(mi))
# print(next(mi))
# print(next(mi))
# print(next(mi))

def yield_test(n):
    for i in range(n):
        tmp = yield i
        print("tmp=", tmp)
    print("Done.")


def call(i):
    return i * 2


for i in yield_test(5):
    print(i, ",")
