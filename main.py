#Juridic
#Postolache Gigi
#Pomana Andreea
#Asofiei Delia

#Importarea librariilor

from urllib.request import urlopen
from bs4 import BeautifulSoup

#Next, declare a variable for the url of the page.
import urllib.request

from settings import WEBSITE_LIST, DEBUG

#specify the url

company_pages = WEBSITE_LIST
#Then, make use of the Python urllib2 to get the HTML page of the url declared.

def get_company_details(company_page):
    page = urllib.request.urlopen(company_page)

    # -------------------------------------------------------------
    soup = BeautifulSoup(page, 'html.parser')
    if (DEBUG):
        print(soup)

    # -------------------------------------------------------------
    # VAR. 1 COMPANY NAME
    # -------------------------------------------------------------

    name_box = soup.find('h1', attrs={'class': "nume_firma"})
    if (DEBUG):
        print(name_box)
    company_name = name_box.text.strip()

    # -------------------------------------------------------------
    # VAR. 2 CUI

    name_box1 = soup.find('h2', attrs={'class': "cui_firma"})

    CUI_firma = name_box1.text.strip()

    # -------------------------------------------------------------

    # -------------------------------------------------------------
    # VAR. 3 CA

    name_box2 = soup.find('span', attrs={'id': "cifra_de_afaceri_box"})
    if (DEBUG):
        print(name_box2)

    CA_firma = name_box2.text.strip()


    # -------------------------------------------------------------

    # VAR. 4 PROFIT

    name_box3 = soup.find('p', attrs={'id': "profit_net_box"})
    if (DEBUG):
        print(name_box3)

    profit_firma = name_box3.text.strip()


    # -------------------------------------------------------------

    # VAR. 5 angajati nr mediu

    name_box4 = soup.find('p', attrs={'id': "numar_angajati_box"})
    if (DEBUG):
        print(name_box4)

    no_angajati = name_box4.text.strip()   


    # -------------------------------------------------------------

    # VAR. 6 Judet

    name_box5 = soup.find('td', attrs={'class': "td_general_info_right td_general_info_right_link_judet_loc"})
    if (DEBUG):
        print(name_box5)

    judet = name_box5.text.strip()   

    return (company_name, CUI_firma, CA_firma, profit_firma, no_angajati, judet)

for company_page in company_pages:
    company_name, CUI_firma, CA_firma, profit_firma, no_angajati, judet = get_company_details(company_page)
    print('Company name: ', company_name)
    print('CUI firma: ', CUI_firma)
    print('CA firma: ', CA_firma)
    print('Profit: ', profit_firma)
    print('Judet: ', judet)
    print('Numar angajati: ', no_angajati)
    print('----------')
    
    
    # -------------------------------------------------------------
    #EXPORTUL DATELOR
    # -------------------------------------------------------------
#1 Tranformarea datelor in format json
#2 Exportul datelor in excel

import json
def saveToFile(data):    
    with open('DEMO.json', 'w') as f:
        json.dump(data, f)

#pip install openpyxl

allData = [] # this is a list
for company_page in company_pages:
    company_name, CUI_firma, CA_firma, profit_firma, no_angajati, judet = get_company_details(company_page)
    product = {} # this is a dictionary
    product['Company name'] = company_name
    product['CUI firma'] = CUI_firma
    product['CA firma'] = CA_firma
    product['Profit'] = profit_firma
    product['Judet'] = judet
    product['Numar angajati'] = no_angajati
    allData.append(product)
    
    print('Company name: ', company_name)
    print('CUI firma: ', CUI_firma)
    print('CA firma: ', CA_firma)
    print('Profit: ', profit_firma)
    print('Judet: ', judet)
    print('Numar angajati: ', no_angajati)
    print('----------')

saveToFile(allData)

import pandas
pandas.read_json("DEMO.json").to_excel("output.xlsx")
