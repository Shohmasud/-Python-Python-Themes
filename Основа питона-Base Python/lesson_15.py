# 15555555
# Функции
# Фу́нкция в программировании, или подпрограмма — фрагмент программного кода,
# к которому можно обратиться из другого места программы.
# 1)определение функции
# 2)тело функции
# 3)вызов функции
# 4)область видимости

# если в теле функции используется print(), то при вызовы ,вызываем только названия самой функции без print()
# def f():#определение функции
#     print('Hello world') #тело функции
# f()# вызов функции

# если в теле функции используется return, то при вызовы функции,вызываем print() внутри названия функции
#def f(): #определение функции
    #return 'Hello world'#тело функции
#print(f())# вызов функции

# Функция с параметрами
# def func(a: int, b: int):
#     return a + b
#
#
# print(func(10, 20))


# def func(a: int, b: int):
#     print(a * b)
#
#
# func(10,20)



# def f(num):
#     sm = 0
#     for i in range(num):
#         sm += i
#         print(i)
#     print(sm)
# f(int(input()))



# sum = 0
# def f1(a):
#     global sum
#     sum += a
#     return f2(int(input()))
# def f2(b):
#     global s
#     sum += b
#     return f3(int(input()))
# def f3(c):
#     global sum
#     sum += c
# f1(10)
# print(sum)

# Рекурсия
# 1)
# def rec(number:int):
#     if number > 0:
#         print(number)
#         number -= 1
#         rec(number)
# rec(10)

# 2)
# def rec(number:int):
#     if number < 6:
#         print(number)
#         number += 1
#         rec(number)
# rec(0)



# передаём внутрь функции кортеж
# 1)
# def f(*numbers):
#     print(numbers)
#
# f(1,2,3,4)

# 2)
# def f(*numbers):
#     print(numbers)
#
# f(*map(int, input().split()))



# передаём внутрь функции список
# 1)
# def f(numbers:list):
#     print(numbers)
# f(list(map(int,input().split())))


# 3)
# def f(numbers:list):
#     print(numbers)
# f([1,2,3,4])



# передаём внутрь функции множество
# def f(numbers:set):
#     print(numbers)
# f(set(map(int,input().split())))


# передаём внутрь функции словари
# def f(**vocabulary):
#     print(vocabulary)
# f(x=10,y=20)

# def f(**vocabulary):
#     print(vocabulary)
# f(x=input(),y=input())


# def f(vocabulary):
#     print(vocabulary)
# f(dict(x=input(), y=int(input())))