
# 21212121
# Полезные методы и функции
# a, b = map(int, input().split())
# print(a,b)

# numbers = [int(n) for n in input().split()]
# print(numbers)

# функция filter
# def f(numbers):
#     if numbers > 0:
#         return numbers
# filter = list(filter(f, map(int, input().split())))
# print(filter)


# лямбда функции
# number = lambda x, y: x + y
# print(number(5,  6))

# пример 2
# def func(a,b):
#     return lambda a, b: a + b
#
#
# f = func(2, 10)
# print(f(10,20))

# пример 3
# def func(a,b):
#     number = lambda n, m: n + m
#     print(number(a, b))
#
#
# func(10, 30)


# пример 4
# def func(b):
#     return lambda a: a - b
#
#
# f = func(2)
# print(f(4))


# пример 5
# for n in range(10):
#     lam = lambda num:num ** 2
#     print(lam(n))


# пример 6
# lm = lambda n : n > 1
# numbers = list(filter(lm, map(int, input().split())))
# print(numbers)


# работа с модулем operator
# пример 1
# import operator
# print(operator.contains([5,6,7], 7))
# print(operator.add(30,20))
# print(operator.mul(3,2))

# пример 2 itemgetter() возврожаем элемент по индексу
# import operator
# numbers = [1,2,3,4,5]
# f = operator.itemgetter(2)
# print(f(numbers))


# пример 3 сортировка элементов списка
# words = [('c','d'), ('e','f'), ('a','b')]
# import operator
# words.sort(key=operator.itemgetter(-1))
# print(words)

# пример с использованием функции partial()
# import operator
# from functools import partial
# words = ['aad','aac', 'aab']
# prt = partial(list.sort,key = operator.itemgetter(-1))
# prt(words)
# print(words)
