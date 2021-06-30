
# 2525252525
# Работа с xml форматом
# Пример 1
# from xml.etree import ElementTree as E
# file = E.parse('xml.xml')
# parse = file.getroot() #получаем корень xml файла
# print(parse)



# Пример 2 получим теги из нашего xml формата
# from xml.etree import ElementTree as E
# file = E.parse('xml.xml')
# parse = file.getroot() #получаем корень xml файла
# tag = parse[0][0].tag
# tag_two = parse[0][1].tag
# print(tag, tag_two)


# Пример 3 получим атрибуты из нашего xml формата
# from xml.etree import ElementTree as E
# file = E.parse('xml.xml')
# parse = file.getroot() #получаем корень xml файла
# tag = parse[0][0].attrib
# tag_two = parse[0][1].attrib
# print(tag, tag_two)



# Пример 4 получим атрибуты из нашего xml формата
# from xml.etree import ElementTree as E
# file = E.parse('xml.xml')
# parse = file.getroot() #получаем корень xml файла
# tag = parse[0][0].attrib
# tag_two = parse[0][1].attrib
# print(tag, tag_two)


# Пример 5 итерируемся по вложеными объектоми
# from xml.etree import ElementTree as E
# file = E.parse('xml.xml')
# parse = file.getroot() #получаем корень xml файла
# for iter in tag.iter():
#     print(iter)

# for iter in tag.iter():
#     print(iter.tag)

# for iter in tag.iter():
#     print(iter.text)

# for iter in parse.iter('boys'):
#     for s in iter:
#         print(s.text)


# Пример 5 создание атрибута xml файле
# from xml.etree import ElementTree as E
# file = E.parse('xml.xml')
# parse = file.getroot() #получаем корень xml файла
# attr = parse[0].set("id", "10")
# file.write('xml.xml') # обновляем файл


# Пример 6 создание атрибута xml файле
# from xml.etree import ElementTree as E
# file = E.parse('xml.xml')
# parse = file.getroot() #получаем корень xml файла
# tag = E.Element('new_tag')
# tag.text = 'hello'
# parse[0][0].append(tag)
# file.write('xml.xml') # обновляем файл



# Пример 6 создание  нашего xml файла изначально
# from xml.etree import ElementTree as E
# students = E.Element('students')
# ratings = E.SubElement(students, 'ratings')
# ratings.set('id', '20')
# girls = E.SubElement(ratings, 'girl')
# girls.set('id', 'girls')
#
# student1 = E.SubElement(girls, 'student1')
# student1.set('id', '1')
# student1.text = '50'
#
# student2 = E.SubElement(girls, 'student2')
# student2.set('id', '2')
# student2.text = '60'
# tag_first = E.ElementTree(students)
# tag_first.write('file_xml.xml')




# Пример 7 нахождение тега из xml файла
# from xml.etree import ElementTree as E
# pr = E.parse('file_xml.xml')
# tag = pr.getroot()
# t = tag[0][0].find('student1')
# print(t.tag, t.attrib)

# Пример 8 удаление тега из xml файла
# from xml.etree import ElementTree as E
# file = E.parse('xml.xml')
# tag = file.getroot()
# t = tag.find('ratings')
# tag.remove(t)
# file.write('xml.xml')
