from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

number_pattern = (\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]
# ((\+7|8)[\s* ]?)?(\(?\d+\)?[\s* ]?)?[\d\- ]{7,10} - находит все номера телефонов
# * с добавочным номером
# \b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b
# r'(\+7|8)?\s*\((\d+)\)\s*(\d+)[-\s]+(\d+)[-\s](\d+)'
number = re.findall(number_pattern, contacts_list)
pprint(number)


