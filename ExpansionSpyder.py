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

def get_url_list (maxyears, maxmonths, maxdays):

    url2 = r"https://www.expansion.com/hemeroteca/"
    url_list = []

    for i in range(0, maxyears):
        url2 = url2 + str(year[i])
        for j in range(0, maxmonths):
            if j <= 9:
                url2 = url2 + '/0' + str(month[j])
            else:
                url2 = url2 + '/' + str(month[j])
            for k in range(0, maxdays):
                if k <= 9:
                    url2 = url2 + '/0' + str(day[k])
                else:
                    url2 = url2 + '/' + str(day[k])
                url_list.append(url2)
                url2 = url2[:-3]
            url2 = url2[:-3]
        url2 = url2[:-4]

    return(url_list)

# listaweb = get_url_expansion(2,11,1)
# print(listaweb)

# driver = webdriver.Chrome()
#
# for i in range(0, len(listaweb)):
#     driver.get(listaweb[i])
#     lista_titulares = driver.find_elements_by_class_name('noticia')
#     print('\n\n' + " - LOS TITULARES DEL " + str(listaweb[i] + '\n\n'))
#
#     for j in range(0, 4):
#         titular = lista_titulares[j].text
#         logging.critical(' [+] ' + titular[:100])
#
#     lista_titulares.clear()
#     sleep(2)
#
# driver.close()
#
# logging.CRITICAL(' ---- End of the program ---- ')