# coding=utf-8
import random
from base import *
i = 0  # переменная-счётчик
i2 = -1  # переменная-счётчик
command = 0  # хранение команды
directory = []  # список с базой
amount = 5  # количество генерируемых записей
amount = int(input('Введите количество генерируемых записей\n'))  # ввод количества

id_t = '\n    ┌──────────────┐\n    │ЗАПИСЬ НАЙДЕНА│\n    └──────────────┘\n\n'
id_f = '\n    ┌─────────────────┐\n    │ЗАПИСЬ НЕ НАЙДЕНА│\n    └─────────────────┘\n\n'


for i in range(amount):
    # определение пола человека по имени и добавление окончания к фамилии
    name_e = name[random.randint(0, len(name)-1)]
    surname_e = surname[random.randint(0, len(surname)-1)]
    if name_e[-1] == 'а' or name_e[-1] == 'я':
        surname_e += 'а'
    # генерация базы
    directory += [[i+1, surname_e, name_e, int(random.randint(80000000000, 89999999999)),
                   street[random.randint(0, len(street)-1)], random.randint(1, 300), random.randint(1, 300)]]

'''''
1 - номер записи
2 - фамилия
3 - имя
4 - номер телефона
5 - название улицы
6 - номер дома
7 - номер квартиры
'''''

while command != 7:
    try:
        command = input('''
    ┌───────────────────────────────────────────┐
    │Введите команду:                                                          │
    │1 - Просмотреть весь справочник                                           │
    │2 - Добавить запись                                                       │
    │3 - Поиск по номеру телефона                                              │
    │4 - Поиск по фамилии                                                      │
    │5 - Поиск по адресу                                                       │
    │6 - Поиск по номеру в базе                                                │
    │7 - Выход                                                                 │
    │Чтобы отменить ввод данных, наберите "вых"                                │
    └───────────────────────────────────────────┘
   ''')
        if command in ['1', '2', '3', '4', '5', '6', '7']:
            command = int(command)
            
            if command == 1:
                # Просмотреть весь справочник
                for i in range(len(directory)):
                    print('\n', directory[i][0],
                          '. Имя: ', directory[i][1], ' ', directory[i][2],
                          '\nТелефон: ', directory[i][3],
                          '\nАдрес: ', directory[i][4],
                          ', дом ', directory[i][5],
                          ', кв. ', directory[i][6],
                          sep='')
                    i += 1
                
            elif command == 2:
                # Добавить запись
                print('\nВведите данные, чтобы добавить новую запись')
                surname_add = input('Фамилия: ')
                if surname_add == 'вых':
                    continue
                name_add = input('Имя: ')
                if name_add == 'вых':
                    continue
                phone_add = input('Телефон: ')
                if phone_add == 'вых':
                    continue
                street_add = input('Улица: ')
                if street_add == 'вых':
                    continue
                number_house_add = input('Дом: ')
                if number_house_add == 'вых':
                    continue
                number_flat_add = input('Квартира: ')
                if number_flat_add == 'вых':
                    continue
                directory += [[len(directory) + 1, surname_add, name_add, int(phone_add),
                               street_add, number_house_add, number_flat_add]]
                print('\nЗапись добавлена')
                
            elif command == 3:
                # Поиск по номеру телефона
                phone_search = input('\nВведите номер телефона: ')
                if phone_search == 'вых':
                    continue
                phone_search = int(phone_search)
                i = 0
                i2 = -1
                while i2 == -1 and i != len(directory):
                    if directory[i][3] == phone_search:
                        i2 = directory[i][0]
                    i += 1
                if i2 != -1:
                    i2 -= 1
                    print(id_t, directory[i2][0],
                          '. Имя: ', directory[i2][1], ' ', directory[i2][2],
                          '\nТелефон: ', directory[i2][3],
                          '\nАдрес: ', directory[i2][4],
                          ', дом ', directory[i2][5],
                          ', кв. ', directory[i2][6],
                          sep='')
                else:
                    print(id_f)

            elif command == 4:
                # Поиск по фамилии
                surname_search = input('\nВведите фамилию: ')
                if surname_search == 'вых':
                    continue
                i = 0
                i2 = -1
                while i2 == -1 and i != len(directory):
                    if directory[i][1] == surname_search:
                        i2 = directory[i][0]
                    i += 1
                if i2 != -1:
                    i2 -= 1
                    print(id_t, directory[i2][0],
                          '. Имя: ', directory[i2][1], ' ', directory[i2][2],
                          '\nТелефон: ', directory[i2][3],
                          '\nАдрес: ', directory[i2][4],
                          ', дом ', directory[i2][5],
                          ', кв. ', directory[i2][6],
                          sep='')
                else:
                    print(id_f)
                
            elif command == 5:
                # Поиск по адресу
                street_search = input('\nВведите название улицы: ')
                if street_search == 'вых':
                    continue
                i = 0
                i2 = -1
                while i2 == -1 and i != len(directory):
                    if directory[i][4] == street_search:
                        i2 = directory[i][0]
                    i += 1
                if i2 != -1:
                    i2 -= 1
                    print(id_t, directory[i2][0],
                          '. Имя: ', directory[i2][1], ' ', directory[i2][2],
                          '\nТелефон: ', directory[i2][3],
                          '\nАдрес: ', directory[i2][4],
                          ', дом ', directory[i2][5],
                          ', кв. ', directory[i2][6],
                          sep='')
                else:
                    print(id_f)
                
            elif command == 6:
                # Поиск по идентификатору в базе
                id_search = input('\nВведите идентификатор: ')
                if id_search == 'вых':
                    continue
                id_search = int(id_search)
                i = 0
                i2 = -1
                while i2 == -1 and i != len(directory):
                    if directory[i][0] == id_search:
                        i2 = directory[i][0]
                    i += 1
                if i2 != -1:
                    i2 -= 1
                    print(id_t, directory[i2][0],
                          '. Имя: ', directory[i2][1], ' ', directory[i2][2],
                          '\nТелефон: ', directory[i2][3],
                          '\nАдрес: ', directory[i2][4],
                          ', дом ', directory[i2][5],
                          ', кв. ', directory[i2][6],
                          sep='')
                else:
                    print(id_f)
        else:
            print('''
    ┌────────────────────────────────────┐
    │НЕВЕРНАЯ КОМАНДА. ПОПРОБУЙТЕ ЕЩЁ РАЗ                          │
    └────────────────────────────────────┘
''')
    except ValueError:
        print('''
    ┌─────────────┐
    │ВВЕДИТЕ ЧИСЛО          │
    └─────────────┘
''')
