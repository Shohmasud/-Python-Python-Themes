
# 29292929
# Конструирование и инициализация.
# __new__(cls, [...)
# __init__(self, [...)
# __del__(self)


# Магические методы сравнения
# __eq__(self, other)
# Определяет поведение оператора равенства, ==.
#
# __ne__(self, other)
# Определяет поведение оператора неравенства, !=.
#
# __lt__(self, other)
# Определяет поведение оператора меньше, <.
#
# __gt__(self, other)
# Определяет поведение оператора больше, >.
#
# __le__(self, other)
# Определяет поведение оператора меньше или равно, <=.
#
# __ge__(self, other)
# Определяет поведение оператора больше или равно, >=.



# Унарные операторы и функции
# _pos__(self)
# Определяет поведение для унарного плюса (+some_object)
#
# __neg__(self)
# Определяет поведение для отрицания(-some_object)
#
# __abs__(self)
# Определяет поведение для встроенной функции abs().
#
# __invert__(self)
# Определяет поведение для инвертирования оператором ~. Для объяснения что он делает смотри статью в Википедии о бинарных операторах.
#
# __round__(self, n)
# Определяет поведение для встроенной функции round(). n это число знаков после запятой, до которого округлить.
#
# __floor__(self)
# Определяет поведение для math.floor(), то есть, округления до ближайшего меньшего целого.
#
# __ceil__(self)
# Определяет поведение для math.ceil(), то есть, округления до ближайшего большего целого.
#
# __trunc__(self)
# Определяет поведение для math.trunc(), то есть, обрезания до целого.



# Обычные арифметические операторы
# __add__(self, other)
# Сложение.
#
# __sub__(self, other)
# Вычитание.
#
# __mul__(self, other)
# Умножение.
#
# __floordiv__(self, other)
# Целочисленное деление, оператор //.
#
# __div__(self, other)
# Деление, оператор /.
#
# __truediv__(self, other)
# Правильное деление. Заметьте, что это работает только когда используется from __future__ import division.
#
# __mod__(self, other)
# Остаток от деления, оператор %.
#
# __divmod__(self, other)
# Определяет поведение для встроенной функции divmod().
#
# __pow__
# Возведение в степень, оператор **.
#
# __lshift__(self, other)
# Двоичный сдвиг влево, оператор <<.
#
# __rshift__(self, other)
# Двоичный сдвиг вправо, оператор >>.
#
# __and__(self, other)
# Двоичное И, оператор &.
#
# __or__(self, other)
# Двоичное ИЛИ, оператор |.
#
# __xor__(self, other)
# Двоичный xor, оператор ^.


# Магические методы преобразования типов

# __int__(self)
# Преобразование типа в int.
#
# __long__(self)
# Преобразование типа в long.
#
# __float__(self)
# Преобразование типа в float.
#
# __complex__(self)
# Преобразование типа в комплексное число.
#
# __oct__(self)
# Преобразование типа в восьмеричное число.
#
# __hex__(self)
# Преобразование типа в шестнадцатиричное число.
#
# __index__(self)
# Преобразование типа к int, когда объект используется в срезах (выражения вида [start:stop:step]). Если вы определяете свой числовый тип, который может использоваться как индекс списка, вы должны определить __index__.
#
# __trunc__(self)
# Вызывается при math.trunc(self). Должен вернуть своё значение, обрезанное до целочисленного типа (обычно long).
#
# __coerce__(self, other)
# Метод для реализации арифметики с операндами разных типов. __coerce__ должен вернуть None если преобразование типов невозможно. Если преобразование возможно, он должен вернуть пару (кортеж из 2-х элементов) из self и other, преобразованные к одному типу.



# Представление своих классов
# __str__(self)
# Определяет поведение функции str(), вызванной для экземпляра вашего класса.
#
# __repr__(self)
# Определяет поведение функции repr(), вызыванной для экземпляра вашего класса. Главное отличие от str() в целевой аудитории. repr() больше предназначен для машинно-ориентированного вывода (более того, это часто должен быть валидный код на Питоне), а str() предназначен для чтения людьми.
#
# __unicode__(self)
# Определяет поведение функции unicode(), вызыванной для экземпляра вашего класса. unicode() похож на str(), но возвращает строку в юникоде. Будте осторожны: если клиент вызывает str() на экземпляре вашего класса, а вы определили только __unicode__(), то это не будет работать. Постарайтесь всегда определять __str__() для случая, когда кто-то не имеет такой роскоши как юникод.
#
# __format__(self, formatstr)
# Определяет поведение, когда экземпляр вашего класса используется в форматировании строк нового стиля. Например, "Hello, {0:abc}!".format(a) приведёт к вызову a.__format__("abc"). Это может быть полезно для определения ваших собственных числовых или строковых типов, которым вы можете захотеть предоставить какие-нибудь специальные опции форматирования.
#
# __hash__(self)
# Определяет поведение функции hash(), вызыванной для экземпляра вашего класса. Метод должен возвращать целочисленное значение, которое будет использоваться для быстрого сравнения ключей в словарях. Заметьте, что в таком случае обычно нужно определять и __eq__ тоже. Руководствуйтесь следующим правилом: a == b подразумевает hash(a) == hash(b).
#
# __nonzero__(self)
# Определяет поведение функции bool(), вызванной для экземпляра вашего класса. Должна вернуть True или False, в зависимости от того, когда вы считаете экземпляр соответствующим True или False.
#
# __dir__(self)
# Определяет поведение функции dir(), вызванной на экземпляре вашего класса. Этот метод должен возвращать пользователю список атрибутов. Обычно, определение __dir__ не требуется, но может быть жизненно важно для интерактивного использования вашего класса, если вы переопределили __getattr__ или __getattribute__ (с которыми вы встретитесь в следующей части), или каким-либо другим образом динамически создаёте атрибуты.
#
# __sizeof__(self)
# Определяет поведение функции sys.getsizeof(), вызыванной на экземпляре вашего класса. Метод должен вернуть размер вашего объекта в байтах. Он главным образом полезен для классов, определённых в расширениях на C, но всё-равно полезно о нём знать.


# Контроль доступа к атрибутам
#
# __getattr__(self, name)
# Вы можете определить поведение для случая, когда пользователь пытается обратиться к атрибуту, который не существует (совсем или пока ещё). Это может быть полезным для перехвата и перенаправления частых опечаток, предупреждения об использовании устаревших атрибутов (вы можете всё-равно вычислить и вернуть этот атрибут, если хотите), или хитро возвращать AttributeError, когда это вам нужно. Правда, этот метод вызывается только когда пытаются получить доступ к несуществующему атрибуту, поэтому это не очень хорошее решение для инкапсуляции.
#
# __setattr__(self, name, value)
# В отличии от __getattr__, __setattr__ решение для инкапсуляции. Этот метод позволяет вам определить поведение для присвоения значения атрибуту, независимо от того существует атрибут или нет. То есть, вы можете определить любые правила для любых изменений значения атрибутов. Впрочем, вы должны быть осторожны с тем, как использовать __setattr__, смотрите пример нехорошего случая в конце этого списка.
#
# __delattr__
# Это то же, что и __setattr__, но для удаления атрибутов, вместо установки значений. Здесь требуются те же меры предосторожности, что и в __setattr__ чтобы избежать бесконечной рекурсии (вызов del self.name в определении __delattr__ вызовет бесконечную рекурсию).
#
# __getattribute__(self, name)
# __getattribute__ выглядит к месту среди своих коллег __setattr__ и __delattr__, но я бы не рекомендовал вам его использовать. __getattribute__ может использоваться только с классами нового типа (в новых версиях Питона все классы нового типа, а в старых версиях вы можете получить такой класс унаследовавшись от object). Этот метод позволяет вам определить поведение для каждого случая доступа к атрибутам (а не только к несуществующим, как __getattr__(self, name)). Он страдает от таких же проблем с бесконечной рекурсией, как и его коллеги (на этот раз вы можете вызывать __getattribute__ у базового класса, чтобы их предотвратить). Он, так же, главным образом устраняет необходимость в __getattr__, который в случае реализации __getattribute__ может быть вызван только явным образом или в случае генерации исключения AttributeError.
# Вы конечно можете использовать этот метод (в конце концов, это ваш выбор), но я бы не рекомендовал, потому что случаев, когда он действительно полезен очень мало (намного реже нужно переопределять поведение при получении, а не при установке значения) и реализовать его без возможных ошибок очень сложно.


# Магия контейнеров
# __len__(self)
# Возвращает количество элементов в контейнере. Часть протоколов для изменяемого и неизменяемого контейнеров.
#
# __getitem__(self, key)
# Определяет поведение при доступе к элементу, используя синтаксис self[key]. Тоже относится и к протоколу изменяемых и к протоколу неизменяемых контейнеров. Должен выбрасывать соответствующие исключения: TypeError если неправильный тип ключа и KeyError если ключу не соответствует никакого значения.
#
# __setitem__(self, key, value)
# Определяет поведение при присваивании значения элементу, используя синтаксис self[nkey] = value. Часть протокола изменяемого контейнера. Опять же, вы должны выбрасывать KeyError и TypeError в соответсвующих случаях.
#
# __delitem__(self, key)
# Определяет поведение при удалении элемента (то есть del self[key]). Это часть только протокола для изменяемого контейнера. Вы должны выбрасывать соответствующее исключение, если ключ некорректен.
#
# __iter__(self)
# Должен вернуть итератор для контейнера. Итераторы возвращаются в множестве ситуаций, главным образом для встроенной функции iter() и в случае перебора элементов контейнера выражением for x in container:. Итераторы сами по себе объекты и они тоже должны определять метод __iter__, который возвращает self.
#
# __reversed__(self)
# Вызывается чтобы определить поведения для встроенной функции reversed(). Должен вернуть обратную версию последовательности. Реализуйте метод только если класс упорядоченный, как список или кортеж.
#
# __contains__(self, item)
# __contains__ предназначен для проверки принадлежности элемента с помощью in и not in. Вы спросите, почему же это не часть протокола последовательности? Потому что когда __contains__ не определён, Питон просто перебирает всю последовательность элемент за элементом и возвращает True если находит нужный.
#
# __missing__(self, key)
# __missing__ используется при наследовании от dict. Определяет поведение для для каждого случая, когда пытаются получить элемент по несуществующему ключу (так, например, если у меня есть словарь d и я пишу d["george"] когда "george" не является ключом в словаре, вызывается d.__missing__("george")).


# Построение дескрипторов
# Чтобы класс стал дескриптором, он должен реализовать по крайней мере один метод из __get__, __set__ или __delete__. Давайте рассмотрим эти магические методы:
#
# __get__(self, instance, instance_class)
# Определяет поведение при возвращении значения из дескриптора. instance это объект, для чьего атрибута-дескриптора вызывается метод. owner это тип (класс) объекта.
#
# __set__(self, instance, value)
# Определяет поведение при изменении значения из дескриптора. instance это объект, для чьего атрибута-дескриптора вызывается метод. value это значение для установки в дескриптор.
#
# __delete__(self, instance)
# Определяет поведение для удаления значения из дескриптора. instance это объект, владеющий дескриптором.



# _new__(cls [,...])	 вызывается при создании экземпляра
# __init__(self [,...]) вызывается при создании экземпляра
# __cmp__(self, other) Вызывается для любого сравнения
# __pos__(self)	+self	Унарный знак плюса
# __neg__(self)	-self	Унарный знак минуса
# __invert__(self)	~self	Побитовая инверсия
# __index__(self)	x[self]	Преобразование, когда объект используется как индекс
# __nonzero__(self)	bool(self), if self:	Булевое значение объекта
# __getattr__(self, name)	self.name # name не определено	Пытаются получить несуществующий атрибут
# __setattr__(self, name, val)	self.name = val	Присвоение любому атрибуту
# __delattr__(self, name)	del self.name	Удаление атрибута
# __getattribute__(self, name)	self.name	Получить любой атрибут
# __getitem__(self, key)	self[key]	Получение элемента через индекс
# __setitem__(self, key, val)	self[key] = val	Присвоение элементу через индекс
# __delitem__(self, key)	del self[key]	Удаление элемента через индекс
# __iter__(self)	for x in self	Итерация
# __contains__(self, value)	value in self, value not in self	Проверка принадлежности с помощью in
# __call__(self [,...])	self(args)	«Вызов» экземпляра
# __enter__(self)	with self as x:	with оператор менеджеров контекста
# __exit__(self, exc, val, trace)	with self as x:	with оператор менеджеров контекста
# __getstate__(self)	pickle.dump(pkl_file, self)	Сериализация
# __setstate__(self)	data = pickle.load(pkl_file)	Сериали



# Пример с методом __new__ и __init__
# class Student(object):
#     def __init__(self, name, lastname):
#         self.name = name
#         self.lastname = lastname
#     def __new__(cls, *args, **kwargs): #конструкция по умолчанию
#         print(f'Это класс Student')
#         return super(cls, Student).__new__(cls)
#
# student = Student('Vasiy', 'Antonov')
# print(student.lastname, student.name)

# сложения
# class Numbers:
#     def __init__(self, x):
#         self.x = x
#     def __add__(self, other):
#         print(self.x + self.x)
# n1 = Numbers(10)
# n2 = Numbers(20)
# n1 + n2


# вычитания
# class Numbers:
#     def __init__(self, x):
#         self.x = x
#     def __sub__(self, other):
#         print(self.x - other.x)
# n1 = Numbers(2)
# n2 = Numbers(2)
# n1 - n2

# возведения в степень
# class Numbers:
#     def __init__(self, x):
#         self.x = x
#     def __pow__(self, power):
#         print(self.x ** power.x)
# n1 = Numbers(2)
# n2 = Numbers(2)
# n1 ** n2


# умножения
# class Numbers:
#     def __init__(self, x):
#         self.x = x
#     def __mul__(self, other):
#         print(self.x * other.x)
# n1 = Numbers(2)
# n2 = Numbers(2)
# n1 * n2



# метод str
# class Student():
#     def __init__(self, name, lastname):
#         self.name = name
#         self.lastname = lastname
#
#     def __str__(self):
#         return 'hello world'
#
# student = Student('Vasiy', 'Antonov')
# print(student)


# метод удаления объектов
# class Student:
#     def __init__(self, name, lastname, box):
#         self.name = name
#         self.lastname = lastname
#         self.box = [1,2,3,4],
#     def __delattr__(se,lf):
#         del  self.name
#
# student = Student('Vasiy', 'Antonov')
# print(student.name)
# del student
# print(student.name)



# class Student:
#     def __init__(self):
#         self.box = ['one','two','three','fore']
#     def __delattr__(self, index):
#         self.box.remove(index)
#         self.box.pop()
#
# student = Student()
# print(student.box)
# del student.one
# print(student.box)


# пример с использованием метода __getattr() __setattr

# __getattr() используется для когда мы вызываем не существующий объект и оно срабатывает
# class Student:
#     def __init__(self, name):
#         self.name = name
#     def __getattr__(self, item):
#         print('Такого атрибута не существует')
#
#
# student = Student('Vasiy')
# student.lastname



# __setattr используется для когда мы присваиваем новое значение атрибуту класса то есть срабатывает
# при присваивании
# class Student:
#     def __setattr__(self, key, value):
#         print('Вы присволи этому атрибуту имя')
#
#
# student = Student()
# student.name = 'Vasily'



# __getattribute__(self, name) используется для того чтобы получить любой атрибут
# class Student:
#     def __init__(self, name, lastname):
#         self.name = name
#         self.lastname = lastname
#     def __getattribute__(self, item):
#         print('Вы вызвали атрибут класса')
#
#
# student = Student('Vasiy', 'Romanov')
# student.lastname


# Контекстный менеджер
# class manager:
#     def __init__(self, file_name, mode):
#         self.file = open(file_name, mode)
#
#     def __enter__(self):
#         return self.file
#
#     def __exit__(self, *args):
#         self.file.close()
#
#
# with manager('test.log', 'w') as f:
#     f.write('hello worlds')