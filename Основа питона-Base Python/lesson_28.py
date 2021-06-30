
# 28282828
# Инкапсуляция- скрытие приватных элементов класса от других объектов.
# class Student:
#     def __init__(self, name, lastname):
#         self._name = name
#         self._lastname = lastname
#     def study(self):
#         print(f'{self._name} {self._lastname} поступил в универcитет')
# student = Student('Vasily', 'Romanov')
# student.study()


# 7пример Конструктор экземпляра класса
# Конструктор используется в классе по умолчанию
# class Student:
#     def __init__(self, name):
#         self.name = name
#
#     # def __new__(cls, *args, **kwargs):
#     #     print(f'Hello студенты')
#     #     sup = super().__new__(cls) #super - это класс object от которого наследуется все пользовательские классы
#     #     return sup
#
#
#     def __new__(cls, *args, **kwargs):
#         print(f'Hello студенты')
#
#
#
# student = Student('Name')






# Наследование- использование методов и атрибутов одного класса(родительского класса) в другом созданном
# классе(дочернем классе)






# class Programmist:
#     def __init__(self, name, year, subject):
#         self.name = name
#         self.year = year
#         self.subject = subject
#     def resolve(self):
#         print(f'Студенты группы {self.name} {self.year}, решают эти задачи в течении семестра')
#
#
#
# class Student(Programmist):
#     def __init__(self,name,lastname, group):
#         self.name = name
#         self.lastname = lastname
#         self.group = group
#
# class Person(Student):
#     def __init__(self, name,lastname, group):
#         self.name = name
#         self.lastname = lastname
#         self.group = group
#
#     def study(self):
#         print(f'{self.lastname} {self.name} поступил в университет')
# programmist = Programmist('Программист', '2021', 'математика, физика, программирования')
# student = Student('Имя', 'Фамилия', 'Группа')
# person = Person('VASILIY', 'ROMANOV', student.group)
# person.study()




# Пример 2
# class Student:
#     def __init__(self,name,lastname, group):
#         self.name = name
#         self.lastname = lastname
#         self.group = group
#
# class Person(Student):
#     def __init__(self, name,lastname, group):
#         super().__init__(name, lastname, group)
#
#     def study(self):
#         print(f'{self.name} учиться в этой группе')
#
# person = Person('Имя', 'Фамилия', 'Группа')
# person.study()



# Пример 3
# class Student:
#     def __init__(self,name,lastname, group):
#         self.name = name
#         self.lastname = lastname
#         self.group = group
#
#     def study(self):
#         print(f'{self.name} учиться в этой группе')
#
# class Person(Student):
#     def __init__(self, name,lastname, group):
#         super().__init__(name, lastname, group)
#     def copy(self):
#         return self.study()
#
#
# person = Person('Имя', 'Фамилия', 'Группа')
# person.copy()





# Полиморфизм - разное поведение одного и того же метода в разных классах.Дочерние классы могут их переопределять
# и решать одну и ту же задачу разными путями,а конкретная реализация будет выбрана только во время исполнения
# программы
# Пример
# class countries:
#     def all_country(self):
#         print('Все страны мира')
#
# class Russia(countries):
#     def __init__(self, name, flag, territory):
#         self.name = name
#         self.flag = flag
#         self.territory = territory
#
#     def description_falg(self):
#         print(f'Флаг {self.name} состоит из {self.flag} цвета')
#
# class India(countries):
#     def __init__(self, name, flag, territory):
#         self.name = name
#         self.flag = flag
#         self.territory = territory
#
#     def description_falg(self):
#         print(f'Флаг {self.name} состоит из {self.flag} цвета')
# countries().all_country()
# russia = Russia('Россия', 'белого, синего и красного', '17 125 191 км²')
# india = India('Индия', 'оранжевого, белого и зеленого', '3 287 263 км²')
# russia.description_falg()
# india.description_falg()


