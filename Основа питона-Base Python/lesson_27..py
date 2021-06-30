# 27272727
# Методы:
# @staticmethod — обычная функция, определенной внутри класса, которая не имеет доступа к экземпляру,
# и ее можно вызывать без создания экземпляра класса.

# Пример:
# class Car(object):
#     def __init__(self, type, name, color):
#         self.type = type
#         self.name = name
#         self.color = color
#
#     @staticmethod
#     def traffic(second, speed):
#         kilometer = speed / 3600
#         sensor = 0
#         for n in range(second):
#             sensor += kilometer
#         print(f'В течении секунд {second}, ваша машина преодолело {sensor} км')
#     @staticmethod
#     def name_class():
#         print('Это класс автомобилей')
# Car('Спортивная машина', 'Модель-BMW M5', 'чёрный')
# Car.traffic(60, 360)
# Car.name_class()






# @classmethod-Методы класса
# @classmethod — это обычный метод класса, имеющий доступ ко всем атрибутам класса, через который он был вызван
# Пример 1
# class Student:
#     def __init__(self, name, last_name, year, subject):
#         self.name = name
#         self.lastname = last_name
#         self.subject = subject
#
#     @classmethod
#     def study(cls):
#         print(f'Студент учиться на программиста')
# Student('Vasya', 'Romanov','22','математика, физика, программирование')
# Student.study()



# Пример 2
# class Student:
#     def __init__(self, name, last_name, year, subject):
#         self.name = name
#         self.lastname = last_name
#         self.subject = subject
#
#     @classmethod
#     def study(cls, Name):
#         print(f'{Name} учиться на программиста')
# student = Student('Vasya', 'Romanov','22','математика, физика, программирование')
# student.study(student.name)


# Пример 3
# class Student:
#     def __init__(self, name, last_name, year, subject):
#         self.name = name
#         self.lastname = last_name
#         self.subject = subject
#
#     @classmethod
#     def study(cls):
#         print(f'Студент учиться на программиста')
#         return cls('Vasya', 'Romanov','22','математика, физика, программирование')
# Student.study()



# Пример 4
# def play(name,last_name, hobby):
#     print(f'{name} {last_name} в свободное время занимается {hobby}')
#
#
# class Student:
#     def __init__(self,year, subject, func):
#         self.subject = subject
#         self.func = func
#
#     def study(self):
#         print(f'Студент учиться на программиста')
#
#     @classmethod
#     def student_play(cls):
#         return cls('22','математика, физика, программирование', play('Vasya','Romanov', 'футболом'))
#
# student = Student
# student.student_play()

z = 'hello'
print(z.upper())