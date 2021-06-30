# 17777777
# Итераторы
# numbers = [1,2,3,4,5]
# for n in numbers:
#     print(numbers)

# n = [1,2,3,4,5]
# numbers = iter(n)
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))



# class list_numbers:
#     def __init__(self, number):
#         self.number = number
#
#     def __next__(self):
#         if self.number < 5:
#             self.number += 1
#             return 'увеличена'
#         else:
#             print(self.number)
#             breakpoint()
#
# num = list_numbers(2)
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))


# class list_numbers:
#     def __init__(self, number):
#         self.number = number
#
#     def __next__(self):
#         if self.number < 5:
#             self.number += 1
#             return 'увеличена'
#         else:
#             print(self.number)
#             breakpoint()
#
# num = list_numbers(2)
# for n in num:
#     print(i)



# class list_numbers:
#     def __init__(self, number):
#         self.number = number
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.number < 5:
#             self.number += 1
#             return 'увеличена'
#         else:
#             print(self.number)
#             breakpoint()
#
# num = list_numbers(2)
# for n in num:
#     print(n)


# Генераторы эффективность – не нужно хранить в памяти всю последовательность, достаточно лишь текущего значения.
# def f(num):
#     for n in range(num):
#         yield n
# func = f(4)
# print(next(func))
# print(next(func))
# print(next(func))
# print(next(func))


# def f(num):
#     for n in range(num):
#         yield n
# for i in f(5):
#     print(i)


# def f(num):
#     for n in range(num):
#         yield n ** 2
# for i in f(5):
#     print(i)