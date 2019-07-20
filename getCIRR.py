#! python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import PyPDF2
from time import sleep

directory = os.getcwd()

for filename in os.listdir(os.getcwd()):
    if filename.endswith('cirrs.pdf'): os.unlink(filename), print('Archivo borrado')

chrome_options = Options()
chrome_options.add_experimental_option('prefs',
                                       {
                                           "download.default_directory": directory,
                                           "download.prompt_for_download": False,
                                           "download.directory_upgrade:": True,
                                           "plugins.always_open_pdf_externally": True
                                       })

browser = webdriver.Chrome(options = chrome_options)
browser.get('http://www.oecd.org/trade/topics/export-credits/documents/cirrs.pdf')
sleep(10)
browser.quit()

pdfFileObj = open('cirrs.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)
texto = pageObj.extractText()
print(texto)
texto_diferente = texto.split()
informacion_util = []
informacion_util.append(texto_diferente[2])
print(informacion_util)
''''
print('CIRR van desde:', texto_diferente[2], "Hasta: ", texto_diferente[4])
print('ACTUAL CIRR DOLAR: REPAYMENT PERIOD >8.5yrs: ', texto_diferente[64])
print('ACTUAL CIRR EURO: REPAYMENT PERIOD > 8.5yrs: ', texto_diferente[70])
print('Los anteriores fueron desde: ', texto_diferente[3], 'hasta: ', texto_diferente[5])
'''