# 111111111
# Списки
# number = [1, 2, 3, 4]
# print(type(number))

# numbers = list(map(int, input().split()))
# print(numbers)

# numbers = list(map(int, input().split()))
# for w in numbers:
#     print(w)

# numbers = list(map(int, input().split()))
# for w in numbers:
#     print(w, end="")



# words = ["один", "два", "три", "четыри", "пять"]
# print(*words)
# print(words[0])
# print(words[-1])

# number = [1, 2, 3, 4, 5, 6]
# print(*number)
# print(number[1])

# number = [1, 2, 3]
# number[0] = 20
# print(number)

# number_word = [1, 2,"один", "два",4, 5]
# for i in number_word:
#     print(i)


# number_word = [1, 2,"один", "два",4, 5]
# for i in range(len(number_word)):
#     print(i, end="")


# вставить элементы
# number = [1, 2, 3]
# number.insert(1, 20)
# print(number)

# добавлять элементы
# number = []
# number.append(4)
# print(number)


# numbers = []
# for n in range(10):
#     numbers.append(n)
# print(numbers)

# добавим элементы в конец массива
# numbers = [1, 2, 3]
# num = [4,5]
# numbers.extend(num)
# print(numbers)

# удалять элементы
# numbers = [1, 2, 3,4,5]
# del numbers[4]
# print(numbers)

# удалить последний элемент
# numbers = [1, 2, 3,4,5]
# numbers.pop()
# print(numbers)

# удалить элементы
# numbers = [1, 2, 3, 4, 5]
# numbers.remove(2)
# numbers.remove(numbers[0])
# print(numbers)

# очищаем список
# words = ["один", "два", "три", "четыри", "пять"]
# print(words.clear())

# копируем список
# words = ["один", "два", "три", "четыри", "пять"]
# numbers = words.copy()
# print(words, numbers, sep="\n")


# считаем количество веденных значений в списке
# numbers = [1,5,5,4,4]
# print(numbers.count(5))

# сортировка списка
# numbers = [2,5,4,1,3,7]
# numbers.sort()
# print(numbers)

# сортировали список а затем перевернули элементы
# numbers = [2,5,4,1,3,7]
# print(*reversed(sorted(numbers)))

# numbers = [2,5,4,1,3,7]
# numbers.sort(reverse=True)
# print(numbers)

# полезные методы
# my_list = [1,2,3,4]
# print(len(my_list))
# print(min(my_list))
# print(max(my_list))
# print(sum(my_list))

# объеденение списков
# box_one = [1,2,3,4]
# box_two = [5, 6]
# print(box_one + box_two)

# numbers = [1]
# print(numbers * 5)

# box_one = [1,2,3,4]
# box_two = [5, 6]
# print(box_one == box_two)

# box_one = list(map(str, input().split()))
# print("".join(box_one))


# words = list("abc dfj hjk")
# print(words)


# numbers = list("12345678")
# print(numbers)


# Тернарный оператор
# nummbers = []
# for n in range(0,11):
#     if n > 5:
#         nummbers.append(n)
# print(nummbers)

# nummbers = [n for n in range(0,11) if n > 5]
# print(nummbers)


# выводим индекс
# my_list = [1, 2, 3, 4]
# print(my_list.index(4))

# метод join
# words = "one, two three"
# box = []
# for w in words:
#     box.append(w)
# print(box)
# print("".join(box))

# sep - разбиение
# end - перенос строки
# \n - разделить строку на новую строку

# метод split
# words = "one two three"
# for w in words.split():
#     print(w)

# words = "one two three"
# for w in words.split():
#     print(''.join(w), end="")

# words = "one two three"
# for w in words:
#     print(w)


# Срезы списков
# my_list = [1, 2, 3, 4]
# print(my_list[0:4])

# my_list = [1, 2, 3, 4]
# print(my_list[0:])

# my_list = [1, 2, 3, 4, 6,7,8,9,10]
# print(my_list[5:9])


# my_list = [1, 2, 3, 4, 6,7,8,9,10]
# for i in my_list[5:9]:
#     print(i, end="")


# words = ["один", "два", "три", "четыри", "пять"]
# print(words[0::2])

# my_list = [1, 2, 3, 4]
# print(my_list[0::2])

# numbers = [1, 2, 3, 4, 6,7,8,9,10]
# print(numbers[::1])
#
# numbers = [1, 2, 3, 4, 6,7,8,9,10]
# print(numbers[::-1])

# words = ["один", "два", "три", "четыри", "пять"]
# print(words[0:9:2])

# num = [1, 2, 3, 4, 6,7,8,9,10]
# print(num[9:0:-2])

# num = [1, 2, 3, 4, 6,7,8,9,10]
# print(num[9:0:-2])