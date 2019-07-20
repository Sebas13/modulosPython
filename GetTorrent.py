#! python3

from selenium import webdriver
from time import sleep

busqueda = 'Billions S06e11'

wd = webdriver.Chrome()
wd.get('https://piratebay-proxylist.se/')
col = wd.find_elements_by_class_name('odd')
col[0].click()

# anuncio = wd.find_element_by_tag_name('body')
# anuncio.click()
# print('Anuncio clicado')

try:

    # DescargarInput = wd.find_element_by_id('inp')
    # DescargarInput.send_keys('Probando')

    sleep(5)

    DescargarInput = wd.find_element_by_id('inp')
    DescargarInput.send_keys('AAAA')
    print(str(DescargarInput))

except:
    print('No se ha encontrado la casilla del input')



# wd.quit()
print('Done')
