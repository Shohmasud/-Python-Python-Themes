# 133333333
# Множество  содержит не повторяющиеся элементы, внутрь не передается списки и словари
# n = {1,2,3,4,5,6,7,8}
# print(n)
# print(type(n))


# n = {1,2,3,3,3,5}
# print(len(n)


# убираем повторящиеся элементы и выводим один раз
# n = {1,2,3,3,3,5}
# print(set(n))

# n = {(1,2),(5,6)}
# print(n)

# конвертация списка в множество
# n = [14,14,14,15]
# s = set(n)
# print(s)

# words = 'hihellohihello'
# print(set(words))

# добавление элементов в множество
# worsd = {'a', 'b', 'c'}
# worsd.add("d")
# print(worsd)


# сортировка множество
# worsd = {'a','b' ,'b', 'b'}
# worsd.add('d')
# sorted(worsd)
# print(worsd)

# worsd = {'a','b' ,'c'}
# sorted(worsd, reverse=True)
# print(worsd)


# удаления элементов множество
# worsd = {'a','c' ,'b', 'b'}
# worsd.remove('a')
# print(worsd)

# удаления последнего элемента множество
# worsd = {'a','c' ,'b', 'b'}
# worsd.pop()
# print(worsd)

# очистка множества
# worsd = {'a','c' ,'b', 'b'}
# worsd.clear()
# print(worsd)

# пересечение &  логический и
# объеденение |  логическое ИЛИ
# разность множеств -
# симметрическая разность ^


# пересечение &  логический и
# a = {1,2,3,4,5}
# b = {1,2,3,4,5,6,7,8,9,10}
# print(a & b)


# объеденение |  логическое ИЛИ
# a = {1,2,3,4,5}
# b = {1,2,3,4,5,6,7,8,9,10}
# print(a | b)


# разность множеств -
# a = {1,2,3,4,5}
# b = {1,2,3,4,5,6,7,8,9,10}
# print(a - b)
# print(b - a)

# симметрическая разность ^
# a = {1,2,3,4,5,11}
# b = {1,2,3,4,5,6,7,8,9,10}
# print(a^b)


# обновить множество
# s = {'a', 'b','c','d'}
# s.update({'i','f','g'})
# print(set(sorted(s)))

# максимальное число
# s = {7,8,9}
# print(max(s))


# минимальное число
# s = {7,8,9}
# print(min(s))

# сумма чисел
# s = {7,8,9}
# print(sum(s))