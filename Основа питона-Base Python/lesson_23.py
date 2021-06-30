# 23232323232
# работа с библиотекой csv



# читаем табличный файл
# import csv
# with open('format_csv.csv', 'r') as file:
#     reader = csv.reader(file)
#     for string in reader:
#         print(string)



# дописываем таблицу в файл
# list = [["10","20","30","40"],
#         ["10","20","30","40"]]
# import csv
# with open('format_csv.csv', 'a') as file:
#     reader = csv.writer(file)
#     reader.writerows(list)


# list = [["10","20","30","40/n"],
#         ["10","20","30","40"]]
# import csv
# with open('format_csv.csv', 'a') as file:
#     reader = csv.writer(file,quoting = csv.QUOTE_ALL)
#     reader.writerows(list)



# list = [["10","20","30","40/n"],
#         ["10","20","30","40"],
#         ["a","b","c","d"]]
# import csv
# with open('format_csv.csv', 'a') as file:
#     reader = csv.writer(file,quoting = csv.QUOTE_NONNUMERIC)
#     reader.writerows(list)


# import csv
# list = [["10","20","30","40/n"],
#         ["10","20","30","40"],
#         ["a","b","c","d"]]
# import csv
# with open('format_csv.csv', 'a') as file:
#     reader = csv.writer(file,delimiter=':')
#     reader.writerows(list)


# функция csv.reader
# функция csv.writer
# класс csv.Dictwriter
# класс csv.DictReader


# delimiter: строка, используемая для разделения полей. По умолчанию это ','.
# double quote: Управляет тем, как должны появляться в кавычках случаи, когда кавычки появляются внутри поля. Может быть True или False.
# escapechar: строка, используемая автором для экранирования разделителя, если в кавычках задано значение QUOTE_NONE.
# lineterminator: строка, используемая для завершения строк, созданных writer. По умолчанию используется значение '\r\n'.
# quotechar: строка, используемая для цитирования полей, содержащих специальные символы. По умолчанию это '"'.
# skipinitialspace: Если установлено значение True, любые пробелы, следующие сразу за разделителем, игнорируются.
# strict: если установлено значение True, возникает Error при неправильном вводе CSV.
# quoting: определяет, когда следует создавать кавычки при чтении или записи в CSV.



