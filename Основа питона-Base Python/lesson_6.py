
# 66666666
# Строки
# hello = 'hell0'
# print(hello)

# hello = "hello"
# print(hello)

# word = 'word'
# print(word)

# сырые строки
# symbol = r'dkdjd$№@&!'
# print(symbol)

# st = "dkdjd$№@&!"
# print(st)


# складываем строки
# print(hello + word)



# умножаем строки
# hi = 'Hi'
# print(hi * 3)

# hi = ' Hi'
# print(hi * 3)


# number = str(5)
# print(number * 10)

# hi = 'Hi'
# world = 'world'
# print(hi, world)
# print(hi + world)
# print(hi ,world, sep='\n')
# print(hi, world, sep='+')



# вхождения строки
# hello = "hello"
# print("he" in hello)
# print("hi" not in hello)





# Форматирование строк
# age = "I am {}".format(70)
# print(age)

# 1 вид
# name = 'Name'
# st = "My name is {}".format(name)
# print(st)


# 2 вид
# name = "Name"
# last_name = f"{name} Lastname"
# print(last_name)


# длина строки
# hello = 'Hello world'
# print(len(hello))


# индекс строки
# hello = 'hello world'
# print(hello[0])



# преобразуем в байт код
# hello = 'hello world'
# print(bytes(hello))


# Срезы
# abcd = 'abcdifghi'
# print(abcd[0:4])

# abcd = 'abcdifghi'
# print(abcd[0:])

# abcd = 'abcdifghi'
# print(abcd[5:9])

# abcd = 'abcdifghi'
# print(abcd[0::2])

# abcd = 'abcdifghi'
# print(abcd[0::2])

# abcd = 'abcdifghi'
# print(abcd[::1])
#
# abcd = 'abcdifghi'
# print(abcd[::-1])

# abcd = 'abcdifghi'
# print(abcd[0:9:2])

# abcd = 'abcdifghi'
# print(abcd[9:0:-2])


# замена слов или же подстроки
# hello = 'hello world'
# print(hello.replace('hello', 'hi'))


# разбиение строки
# good_morning = 'Good,morning,hello,world'
# print(good_morning.split(","))

# good_morning = 'Good , morning , hello , world'
# print(good_morning.split())

# функция join
# good_morning = 'Goodmorninghelloworld'
# print('-'.join(good_morning))


# good_morning = 'Goodmorning,helloworld'
# print('!'.join(good_morning.split(',')))
# print(' '.join(good_morning.split(',')))


# abc = 'a,b,c,d,i,f'
# print('$'.join(abc.rsplit(',')))
# print(' '.join(abc.rsplit(',')))


# состоит ли строка из цифр
# age = 'age'
# num = 70
# print(num + age.isdigit())



# состоит ли строка из букв
# hi = 'hi'
# print(hi.isalpha())


# состоит ли строка из букв и цифр
# st = 'aabasbsdf548'
# print(st.isalnum())


# cостоит ли строка из символов только в нижнем регистре
# st = 'abcd'
# print(st.islower())


# cостоит ли строка из символов только в  верхнем регистре
# st = 'ABCD'
# print(st.isupper())


# преобразование строки к верхнему регистру
# abc = 'abcdD'
# print(abc.upper())


# преобразование строки к нижнему регистру
# abc = 'abcdABCD'
# print(abc.lower())


# начинаются ли слова в строке с заглавной буквы
# hi  = 'hi'
# print(hi.istitle())


# начало строки
# hello = 'hello world'
# print(hello.startswith("hello"))
# print(hello.startswith("world"))


# конец строки
# hello = 'hello world'
# print(hello.endswith("hello"))
# print(hello.endswith("world"))


# убираем символы в строке
# st = '?ifgh!,'
# print(st.strip("?!,"))

# убираем символы справа
# st = '?ifgh!!'
# print(st.rstrip("?!"))

# убираем символы слева
# st = '?$$ifgh!!'
# print(st.lstrip("?$$"))
