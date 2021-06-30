
# 3131313131
# Отладка и тестирование

# Отладка программы
# import pdb
# import unittest
# class Person(unittest.TestCase):
#
#     def __init__(self, name, lastname):
#         self.name = name
#         self.lastname = lastname
#
#     def __get__(self, instance, owner):
#         # pdb.set_trace()
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
#
#
# if __name__ == '__main__':
#     student = Student()
#     student.attribute
#     student.attribute = 'Name'
#     student.attribute = 'Lastname'
#     del student.attribute

# Тестирование
# import unittest
# class Person(unittest.TestCase):
#     def setUp(self):
#         pass
#
#     def tearDown(self):
#         pass
#
#     def __init__(self, name, lastname):
#         self.name = name
#         self.lastname = lastname
#
#     def __get__(self, instance, owner):
#         # pdb.set_trace()
#         print('Сработало метод get')
#
#
#     def __set__(self, instance, value):
#         print('Сработало метод set')
#         for n in range(100000):
#             print(n)
#
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
#
#
# if __name__ == '__main__':
#     student = Student()
#     student.attribute
#     student.attribute = 'Name'
#     student.attribute = 'Lastname'
#     del student.attribute
#     unittest.main()


# setUp – подготовка прогона теста; вызывается перед каждым тестом.
# tearDown – вызывается после того, как тест был запущен и результат записан. Метод запускается даже в случае исключения (exception) в теле теста.
# setUpClass – метод вызывается перед запуском всех тестов класса.
# tearDownClass – вызывается после прогона всех тестов класса.
# setUpModule – вызывается перед запуском всех классов модуля.
# tearDownModule – вызывается после прогона всех тестов модуля.


# Модуль unittest предоставляет множество функций для самых различных проверок:
#
# assertEqual(a, b) — a == b
#
# assertNotEqual(a, b) — a != b
#
# assertTrue(x) — bool(x) is True
#
# assertFalse(x) — bool(x) is False
#
# assertIs(a, b) — a is b
#
# assertIsNot(a, b) — a is not b
#
# assertIsNone(x) — x is None
#
# assertIsNotNone(x) — x is not None
#
# assertIn(a, b) — a in b
#
# assertNotIn(a, b) — a not in b
#
# assertIsInstance(a, b) — isinstance(a, b)
#
# assertNotIsInstance(a, b) — not isinstance(a, b)
#
# assertRaises(exc, fun, *args, **kwds) — fun(*args, **kwds) порождает исключение exc
#
# assertRaisesRegex(exc, r, fun, *args, **kwds) — fun(*args, **kwds) порождает исключение exc и сообщение соответствует регулярному выражению r
#
# assertWarns(warn, fun, *args, **kwds) — fun(*args, **kwds) порождает предупреждение
#
# assertWarnsRegex(warn, r, fun, *args, **kwds) — fun(*args, **kwds) порождает предупреждение и сообщение соответствует регулярному выражению r
#
# assertAlmostEqual(a, b) — round(a-b, 7) == 0
#
# assertNotAlmostEqual(a, b) — round(a-b, 7) != 0
#
# assertGreater(a, b) — a > b
#
# assertGreaterEqual(a, b) — a >= b
#
# assertLess(a, b) — a < b
#
# assertLessEqual(a, b) — a <= b
#
# assertRegex(s, r) — r.search(s)
#
# assertNotRegex(s, r) — not r.search(s)
#
# assertCountEqual(a, b) — a и b содержат те же элементы в одинаковых количествах, но порядок не важен