#Juridic
#Asofiei Delia
#Pomana Andreea
#Postolache Gigi

#Instalarea pachetului pip
#conda install - c anaconda pip 

#Instalarea librariei
#pip install BeautifulSoup4

#*******ANDREEA POMANA*******
#Importarea librariilor

from urllib.request import urlopen
from bs4 import BeautifulSoup

#Next, declare a variable for the url of the page.
import urllib.request

#specify the url

company_page = 'https://www.romanian-companies.eu/omv-petrom-sa-1590082/'
#Then, make use of the Python urllib2 to get the HTML page of the url declared.

page = urllib.request.urlopen(company_page)

#-------------------------------------------------------------
soup = BeautifulSoup(page, 'html.parser')

# first table

# stergem caracterele speciale dintr-un sir de caractere
def replace_special(web_string):
    web_string = web_string.replace('\r\n', '')
    web_string = web_string.replace('\n', '')
    web_string = web_string.replace('\xa0', '')
    return web_string

extrase_tabel = {}
primul_tabel = soup.find('table', attrs={'id': 'date-de-identificare'})
randuri_tabel = primul_tabel.find_all('tr', attrs={'': ''})
for rand_tabel in randuri_tabel:
    coloane = rand_tabel.find_all('td', attrs={'': ''})
    if(len(coloane) == 2):
        # stergem caracterele speciale
        key = replace_special(coloane[0].text)
        value = replace_special(coloane[1].text)
        extrase_tabel[key] = value
print(extrase_tabel)

#*******ANDREEA POMANA*******


#-------------------------------------------------------------
#ASOFIEI DELIA

#Compania lUKOIL
company_page2 = 'https://www.romanian-companies.eu/lukoil-romania-srl-10547022/'
page2 = urllib.request.urlopen(company_page2)

#-------------------------------------------------------------
soup = BeautifulSoup(page2, 'html.parser')

# second table

# stergem caracterele speciale dintr-un sir de caractere
def replace_special(web_string):
    web_string = web_string.replace('\r\n', '')
    web_string = web_string.replace('\n', '')
    web_string = web_string.replace('\xa0', '')
    return web_string

extrase_tabel2 = {}
second_tabel = soup.find('table', attrs={'id': 'date-de-identificare'})
randuri_tabel2 = second_tabel.find_all('tr', attrs={'': ''})
for rand_tabel2 in randuri_tabel2:
    coloane = rand_tabel2.find_all('td', attrs={'': ''})
    if(len(coloane) == 2):
        # stergem caracterele speciale
        key = replace_special(coloane[0].text)
        value = replace_special(coloane[1].text)
        extrase_tabel2[key] = value
print(extrase_tabel2)


#-------------------------------------------------------------
#Compania SOCAR
#POSTOLACHE GIGI
# third table

company_page3 = 'https://www.romanian-companies.eu/socar-petroleum-sa-12546600/'

page3 = urllib.request.urlopen(company_page3)

#-------------------------------------------------------------
soup = BeautifulSoup(page3, 'html.parser')

# second table

# stergem caracterele speciale dintr-un sir de caractere
def replace_special(web_string):
    web_string = web_string.replace('\r\n', '')
    web_string = web_string.replace('\n', '')
    web_string = web_string.replace('\xa0', '')
    return web_string

extrase_tabel3 = {}
third_tabel = soup.find('table', attrs={'id': 'date-de-identificare'})
randuri_tabel3 = third_tabel.find_all('tr', attrs={'': ''})
for rand_tabel3 in randuri_tabel3:
    coloane = rand_tabel3.find_all('td', attrs={'': ''})
    if(len(coloane) == 2):
        # stergem caracterele speciale
        key = replace_special(coloane[0].text)
        value = replace_special(coloane[1].text)
        extrase_tabel3[key] = value
print(extrase_tabel3)



