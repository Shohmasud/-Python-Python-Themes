# 30303030
# Дискрипторы
# Пример
# class Person:
#     def __init__(self, name, lastname):
#         self.name = name
#         self.lastname = lastname
#     def __get__(self, instance, owner):
#         print('Сработало метод get')
#
#
#     def __set__(self, instance, value):
#         print('Сработало метод set')
#         i = 0
#         if i == 0:
#             self.name = value
#             print(f'Имя студента:{self.name}')
#             i += 1
#         else:
#             self.lastname = value
#             print(f'Фамилия студента:{self.lastname}')
#
#     def __delete__(self, instance):
#         print('Сработало метод del')
#
#
# class Student:
#     attribute = Person(None, None)
# student = Student()
# student.attribute
# student.attribute = 'Name'
# student.attribute = 'Lastname'
# del student.attribute


# Метаклассы-это когда класс создает другие классы
# class Meta_class(type):
#     def __init__(cls, name_class, bases,atrr):
#         print(f'Названия класса {name_class}')
#         if not hasattr(cls, 'attribute'):
#             cls.attribute = {}
#         else:
#             cls.attribute[name_class] = cls
#         super().__init__(name_class, bases, atrr)
# class A(metaclass=Meta_class):
#     pass
# class B(A):
#     pass
# class C(A):
#     pass
# print(A.attribute)
