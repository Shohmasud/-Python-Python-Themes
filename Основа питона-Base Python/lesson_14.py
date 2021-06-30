
# 1444444444
# Словари
# Словари в Python - неупорядоченные коллекции произвольных объектов с доступом по ключу
# country = {}
# print(type(country))


# country = {'Moscow':'Russia', 'Stambul':'Turkey', 'Dehli':'India'}
# print(country)

# добавить новые элементы в слоаврь
# country = {'Moscow':'Russia', 'Stambul':'Turkey', 'Dehli':'India'}
# country['Sofia'] = 'Bulgaria'
# print(country)


# очищаем словарь
# country = {'Moscow':'Russia', 'Stambul':'Turkey', 'Dehli':'India'}
# country.clear()
# print(country)


# удаляем элементы словаря
# country = {'Moscow':'Russia', 'Stambul':'Turkey', 'Dehli':'India'}
# del country['Moscow']
# print(country)


# обновляем словарь
# country = {'Moscow':'Russia', 'Stambul':'Turkey', 'Dehli':'India'}
# add_dict ={'Sofia':'Bulgaria'}
# country.update(add_dict)
# print(country)



# обращение по ключу
# country = {'Moscow':'Russia', 'Stambul':'Turkey', 'Dehli':'India'}
# print(country['Stambul'])

# метод dict
# country = dict(Moscow='Russia', Stambul='Turkey', Dehli='India')
# print(country)

# country = dict([(1,2), (3,4)])
# print(country)


# если к каждому отдельному ключу сопоставить одинаковые значение то используют метод fromkeys
# country = dict.fromkeys(['Moscow', 'Sochi', 'Volgograd'], 'Russia')
# print(country)

#  получения значения словаря
# country = {'Moscow':'Russia', 'Stambul':'Turkey', 'Dehli':'India'}
# print(country.values())


# получения ключей словаря
# country = {'Moscow':'Russia', 'Stambul':'Turkey', 'Dehli':'India'}
# print(country.keys())

# перебор циклом словаря
# country = {'Moscow':'Russia', 'Stambul':'Turkey', 'Dehli':'India'}
# for k in country:
#     print(k)


# country = {'Moscow':'Russia', 'Stambul':'Turkey', 'Dehli':'India'}
# for k in country:
#     print(k, country[k], sep='-')


# country = {'Moscow':'Russia', 'Stambul':'Turkey', 'Dehli':'India'}
# for key in country.keys():
#     print(key)


# country = {'Moscow':'Russia', 'Stambul':'Turkey', 'Dehli':'India'}
# for value in country.values():
#     print(value)


# country = {'Moscow':'Russia', 'Stambul':'Turkey', 'Dehli':'India'}
# for val, key in country.items():
#     print(val, key)


# Сортировка словаря по ключу
# country = {'Moscow':'Russia', 'Stambul':'Turkey', 'Dehli':'India'}
# for country in sorted(country.items() , key= lambda x: x[0]):
#     print(country)


# country = {'Moscow':'Russia', 'Stambul':'Turkey', 'Dehli':'India'}
# for country in sorted(country.items() , key= lambda x: x[1]):
#     print(country)


# проверка на вхождения
# country = {'Moscow':'Russia', 'Stambul':'Turkey', 'Dehli':'India'}
# for w in country:
#     if w in country:
#         print(w)


# составление словаря тернарным способом
# numbers = {n : n + 2 for n in range(10)}
# print(numbers)

# numbers = dict()
# for n in range(10):
#     numbers[n] = n + 2
# print(numbers)

# вложения внутри словаря
# numbers = {0:['ноль', 'один', 'два']}
# print(numbers)
# print(numbers[0][0])


# numbers = {0:('ноль', 'один')}
# print(numbers)
# print(numbers[0][0])