
# 2424242424
# Работа с json форматом
# чтобы вывести сразу сразу не из файла то используем dumps
# import json
# dictionary = {'student1':10,
#               'student2':20,
#               'student3':30,
#               'student4':40,}
#
# print(json.dumps(dictionary))


# чтобы дописать результат в файл то используем dump
# import json
# dictionary = {'student1':10,
#               'student2':20,
#               'student3':30,
#               'student4':40,}
#
# with open('format_json.json', 'a') as file:
#     json.dump(dictionary,file, indent=3)


# когда сразу читаем json формат
# import json
# dictionary = {'student1':10,
#               'student2':20,
#               'student3':30,
#               'student4':40,}
#
# json_dumps = json.dumps(dictionary)
# json_load = json.loads(json_dumps)
# print(json_load)



# когда читаем из файла json формат
# import json
# with open('format_json.json', 'r') as file:
#     print(json.load(file))
