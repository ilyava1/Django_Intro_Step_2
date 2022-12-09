import csv
from django.core.management.base import BaseCommand
from phones.models import Phone
from datetime import datetime


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)
            print()
            str=''
            for line in phone_reader:
                # print('*'*50)
                # print('type(line[1]) = ',type(line[1]))
                ph_model = line[1].split(sep=' ', maxsplit=-1)
                spaces_qua = len(ph_model) - 1
                # print('строка для обработки = ', line[1])
                # print('список для обработки = ', ph_model)
                slug_str = ''
                for string_part in ph_model:
                    slug_str += string_part
                    if spaces_qua > 0:
                        slug_str += '_'
                        spaces_qua -= 1
                # print('Получена slug_str = ', slug_str)
                # print('*' * 50)
                current_phone = Phone(name=line[1], image=line[2],
                                      price=float(line[3]), release_date=line[4],
                                      lte_exists=bool(line[5]), slug=slug_str)
                current_phone.save()
                print('Телефон - ', current_phone, ' - сохранен в БД')
                print()
            print('Загрузка каталога телефонов в БД завершена')
            print()
