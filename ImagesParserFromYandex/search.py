import requests
import os.path
from ImageParser import YandexImage

parser = YandexImage()

n = int(input("Введите количество желаемых запросов: "))
linktofile = input('Введите путь, куда хотите сохранять изображения: ')

#Скачивание картинок по ссылке(30 штук)
num = 1
while num <= n:
    namejpg = 1
    errornum = 1
    filename = str(input('Введите название файла: '))
    zapros = str(input("Введите запрос: "))
    os.mkdir(str(linktofile) + '/' + str(filename))
    try:
        os.chdir(str(linktofile) + '/' + str(filename))
        def download_image(url):
            fullnamejpg = str(namejpg) + ".jpg"
            p = requests.get(itemurl)
            out = open(fullnamejpg, "wb")
            out.write(p.content)
            out.close()
        for item in parser.search(zapros):
            try:
                itemurl = item.url
                download_image(str(itemurl))
                namejpg += 1
                errornum += 1
            except:
                print("Ошибка скачивания картинки по ссылке:", errornum)
                errornum += 1
        num += 1
    except:
        print("Введите другое название папки и запрос заново")

    # Запись ссылок в файл(по 30 штук)
    with open('res.txt', "a") as file:
        for item in parser.search(zapros):
            file.write(item.url + '\n')
