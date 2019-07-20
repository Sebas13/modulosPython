#! python3

# import speech_recognition
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import random

import os
import PyPDF2
from time import *


def automateInmigrationShit():

    chrome_options = Options()
    chrome_options.add_experimental_option('prefs',
                                       {
                                           "download.prompt_for_download": False,
                                           "download.directory_upgrade:": True,
                                           "plugins.always_open_pdf_externally": True
                                       })

    browser = webdriver.Chrome(options = chrome_options)
    browser.maximize_window()
    browser.get('https://sede.administracionespublicas.gob.es/icpplustiem/index.html')

    s1 = Select(browser.find_element_by_id('form'))
    s1.select_by_index(29)
    CookiesElement = browser.find_element_by_id('cookie_action_close_header')
    CookiesElement.click()
    sleep(1)
    ButtonElement = browser.find_element_by_id('btnAceptar')
    ButtonElement.click()
    sleep(1)
    s2 = Select(browser.find_element_by_id('tramite'))
    s2.select_by_index(8)
    sleep(random.randint(1,4))
    ButtonElement2 = browser.find_element_by_id('btnAceptar')
    ButtonElement2.click()
    sleep(1)
    ButtonElement3 = browser.find_element_by_id('btnEntrar')
    ButtonElement3.click()
    ButtonRadioElement = browser.find_element_by_id('rdbTipoDocPas')
    ButtonRadioElement.click()
    PassportElement = browser.find_element_by_id('txtIdCitado')
    PassportElement.send_keys('728859655')
    NombreElement = browser.find_element_by_id('txtDesCitado')
    NombreElement.send_keys('VERONICA ALCHAKOVA')
    YearElement = browser.find_element_by_id('txtAnnoCitado')
    YearElement.send_keys('1998')
    s3 = Select(browser.find_element_by_id('txtPaisNac'))
    s3.select_by_index(158)
    sleep(1)
    browser.quit()
    print('OK')

intento = 0

for i in range(10):
    automateInmigrationShit()
    intento += 1
    print('[+] Hemos intentado reventar a esta puta ' + str(intento) + ' veces [+]')