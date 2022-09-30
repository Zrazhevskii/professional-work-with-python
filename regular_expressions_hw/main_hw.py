import re
from pprint import pprint
import csv

phone_find = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
phone_sub = r'+7(\2)-\3-\4-\5 \6\7'

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def main(contact_list: list):
    new_list = list()
    for contact in contact_list:
        full_name = ' '.join(contact[:3]).split(' ')
        contact[5] = re.sub(phone_find, phone_sub, contact[5])
        result = [full_name[0], full_name[1], full_name[2], contact[3], contact[4], contact[5], contact[6]]
        new_list.append(result)
    return union(new_list)


def union(contacts: list):
    for contact in contacts:
        last_name = contact[0]
        first_name = contact[1]
        for new_contact in contacts:
            new_last_name = new_contact[0]
            new_first_name = new_contact[1]
            if last_name == new_last_name and first_name == new_first_name:
                if contact[2] == "":
                    contact[2] = new_contact[2]
                elif contact[3] == "":
                    contact[3] = new_contact[3]
                elif contact[4] == "":
                    contact[4] = new_contact[4]
                elif contact[5] == "":
                    contact[5] = new_contact[5]
                elif contact[6] == "":
                    contact[6] = new_contact[6]

    result_list = list()
    for i in contacts:
        if i not in result_list:
            result_list.append(i)
    # pprint(result_list)
    return write_file(result_list)


def write_file(result_list):
    with open("phonebook.csv", "w", encoding="utf-8") as file:
        data_writer = csv.writer(file, delimiter=',')
        data_writer.writerows(result_list)


if __name__ == '__main__':
    main(contacts_list)

