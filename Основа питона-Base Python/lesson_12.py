
# 12222222
# Кортежи
# обозначаются круглыми скобками
# упорядочены по позициям;
# tuple могут хранить и содержать внутри себя объекты любых типов (и даже составных);
# доступ к элементам происходит по смещению, а не по ключу;
# в рамках этой структуры данных определены все операции, основанные на применении смещения (индексирование, срез);
# кортежи поддерживают неограниченное количество уровней вложенности;


# number = (1,2,3)
# print(type(number))


# word = tuple("hello")
# print(word)



# word = ("h", "e", "l", "l", "o")
# print(word)
# print(*word)


# numbers = (4,7,8,9,10)
# print(*numbers)

# numbers = (4,7,8,9,10)
# print(numbers[0])

# numbers = (4,7,8,9,10)
# numbers[0] = 5
# print(numbers)


# numbers = ((4,7),(8,9),[10,2])
# print(numbers)

# numbers = ((4,7),(8,9),[10,2])
# print(numbers[2][0])


# numbers = ((4,7),(8,9),[10,2])
# for i in numbers[2]:
#     print(i)


# numbers = (1,58,10,11)
# print(len(numbers))


# Сравнение кортежей
# a = ("a")
# b = ("i")
# print(a < b)


# x = (5,50,50,50,50)
# y = (10,12,13)
# print(x < y)


# операции с кортежами
# сложение
# x = (1,2,3,4)
# y = (5,6,7)
# print(x + y)

# Умножение
# x = (1,2,3,4)
# print(x*3)

# длина
# numbers = ((1,2),(10,20),(30,40))
# print(len(numbers))

# число встречающихся чисел
# numbers = ((1,2),(10,20),(30,40))
# print(numbers[1].count(10))

# максимальное число
# numbers = (1,2,3,50)
# print(max(numbers))

# минимальное число
# numbers = (1,2,3,50)
# print(min(numbers))


# сумма чисел в кортежи
# numbers = (1,2,3)
# print(sum(numbers))


# сортировка
# numbers = (2,3,50,20,10,40)
# sorted(numbers)
# print(numbers)


# индекс
# numbers = (1,2,3)
# print(numbers.index(2))


# срезы
# numbers = (2,3,50,20,10,40,50,60,70)
# print(numbers[0:5])
# print(numbers[5:8])
# print(numbers[::2])
# print(numbers[1::3])
# print(numbers[1:6:3])


# a = ((8,9,7,5,6),[1,2,5,6],{1,2,3,4},{"a":2,"b":4})
# print(a)


# выводим повторящиеся числа
# numbers = (2,2,2,3,3)
# print(set(numbers))