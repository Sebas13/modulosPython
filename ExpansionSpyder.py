from selenium import webdriver
from time import sleep
import logging

#Codigo para logging

logging.basicConfig(level=logging.CRITICAL, format = ' %(message)s')

logging.critical('---- Start of the program ---- ')

#Rastrear Hemeroteca de expansion

year = [2016,2017,2018,2019] # La hemeroteca antes de 2016 tiene otro formato, tengo que haccer una araña diferentes para años antes del 2016
month = [1,2,3,4,5,6,7,8,9,10,11,12]
day = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
listaweb = []

def create_url(day, month, year):

    url = r"https://www.expansion.com/hemeroteca/"

    #Format month and day so if it is less than 10, put a zero before
    if month < 10:
        month = "/0" + str(month)
    else:
        month = "/" + str(month)

    if day < 10:
        day = "/0" + str(day)
    else:
        day = "/" + str(day)

    url2 = url + str(year) + month + day
    return url2

for i in range(2):
    listaweb.append(create_url(i,month[8], year[2])) #Primeros dos dias de Septiembre de 2018


driver = webdriver.Chrome()

for i in range(0, len(listaweb)):

    dia = listaweb[i][-2:]
    mes = listaweb[i][-5 : -3]
    ano = listaweb[i][-10 : -6]

    driver.get(listaweb[i])
    lista_titulares = driver.find_elements_by_class_name('noticia')
    print('\n\n' + " [+] Los titulares del día " + str(dia) + " de " + str(mes) + " de " + str(ano) + '\n\n')

    for j in range(0, len(lista_titulares)):
        titular = lista_titulares[j].text
        logging.critical(' [!] ' + titular)

    lista_titulares.clear()
    sleep(2)

driver.close()

logging.CRITICAL(' ---- End of the program ---- ')