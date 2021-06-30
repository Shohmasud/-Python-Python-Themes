# 199999
# Работа с файлами
# 'r'	открытие на чтение (является значением по умолчанию).
# 'w'	открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
# 'x'	открытие на запись, если файла не существует, иначе исключение.
# 'a'	открытие на дозапись, информация добавляется в конец файла.
# 'b'	открытие в двоичном режиме.
# 't'	открытие в текстовом режиме (является значением по умолчанию).
# '+'	открытие на чтение и запись

# пример 1
# f = open('text_file.txt', 'r')
# print(f.read())
# f.close()

# f = open('text_file.txt', 'r')
# print(f.read())
# f.close()

# f = open('text_file.txt', 'r')
# print(f.readline())
# f.close()

# пример 2
# f = open('text_file.txt', 'r') as file
# print(file.read())
# f.close()

# пример 3
# f = open('text_file.txt', 'r')
# print(f.read(10))
# f.close()

# пример 4
# f = open('text_file.txt', 'r')
# for w in f:
#     print(w)
# f.close()



# пример 5
# f = open('text_file.txt', 'w')
# f.write('Hi\n')
# f.close()

# пример 6
# f = open('text_file.txt', 'a')
# f.write('Hi\n')
# f.close()

# пример 7
# f = open('text_file.txt', 'a')
# lst = ['hi', 'hello', 'world']
# for w in lst:
#     f.write(f'{w}\n')
# f.close()


# чтобы узнать адрестекущей папки
# import os
# print(os.getcwd())

# выводим все файлы данной папки
# import os
# print(os.listdir())
# print(os.listdir('.idea'))

# чтобы узнать что файл существует
# import os.path
# print(os.path.exists('lesson_1.py'))

# чтобы узнать какой путь является папкой
# import os.path
# print(os.path.isdir('D:\pythonn_filee'))
# print(os.path.isdir('.idea'))


# чтобы узнать какой путь является файлом
# import os.path
# print(os.path.isfile('lesson_1.py'))

# чтобы менять директории
# import os
# print(os.getcwd())
# os.chdir('webdraive')
# print(os.getcwd())


# чтобы копировать файлы используем
# import shutil
# shutil.copy('lesson_1.py', 'file')
# shutil.copytree('file_two', 'file_two/lesson_1.py')

