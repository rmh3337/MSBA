# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 12:24:45 2019

@author: 19785
"""

import re
from _pickle import dump
import requests
import pandas as pd

ticker = input('Enter the ticker of the company you want to search:\n')
DEFAULT_TICKERS = [ticker]
URL = 'http://www.sec.gov/cgi-bin/browse-edgar?CIK={}&Find=Search&owner=exclude&action=getcompany'
CIK_RE = re.compile(r'.CIK=(\d{10}).')

cik_dict = {}
for ticker in DEFAULT_TICKERS:
    f = requests.get(URL.format(ticker), stream=True);
    results = CIK_RE.findall(f.text)
if len(results):
    cik_dict[str(ticker).lower()] = str(results[0])

stock = results[0]


import re
gross_profit = []
tax = []
sga = []
dep = []
amor = []
ass_cur = []
lia_cur = []
ppe = []
interest = []
ltd = []

# regex = ['', '\w*']

years = [2018]
gaap_list = [gross_profit, tax, sga, dep, amor, ass_cur, lia_cur, ppe, interest, ltd]


for year in years:
    from bs4 import BeautifulSoup
    import requests
    import sys

    # Access page
    cik = stock
    type = '10-K'
    dateb = '20191101'

    # Obtain HTML for search page
    base_url = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={}&type={}&dateb={}"
    edgar_resp = requests.get(base_url.format(cik, type, dateb))
    edgar_str = edgar_resp.text

    # Find the document link
    doc_link = ''
    soup = BeautifulSoup(edgar_str, 'html.parser')
    table_tag = soup.find('table', class_='tableFile2')
    rows = table_tag.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
    #     print(cells)
        if len(cells) > 3:
            if str(year) in cells[3].text:
                doc_link = 'https://www.sec.gov' + cells[1].a['href']

    # Exit if document link couldn't be found
    if doc_link == '':
        print("Couldn't find the document link")
        sys.exit()

    # Obtain HTML for document page
    doc_resp = requests.get(doc_link)
    doc_str = doc_resp.text

    # Find the XBRL link
    xbrl_link = ''
    soup = BeautifulSoup(doc_str, 'html.parser')
    table_tag = soup.find('table', class_='tableFile', summary='Data Files')
    rows = table_tag.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        if len(cells) > 3:
            if 'INS' in cells[3].text:
                xbrl_link = 'https://www.sec.gov' + cells[2].a['href']

    # Obtain XBRL text from document
    xbrl_resp = requests.get(xbrl_link)
    xbrl_str = xbrl_resp.text
    
    # Find and print stockholder's equity
    soup = BeautifulSoup(xbrl_str, 'lxml')
    tag_list = soup.find_all([re.compile('us-gaap:')])
                           
    gaap_words = ['grossprofit', 'taxes', 'generalandadministrative', 'depreciation',  'amortization', 'assetscurrent',
           'liabilitiescurrent', 'paymentstoacquirepropertyplantandequipment', 'interestexp', 'longtermdebtnon']
  
    for y in range(len(gaap_words)):
        for tag in tag_list:
            stuff = re.findall('\w*'+gaap_words[y]+'\w*', tag.name)
            if stuff != []:
                if stuff[0] not in gaap_list[y]:
                    gaap_list[y].append(stuff[0])                    

                     
print('\n\n\tPlease select the proper items from above for each of the following sections\n')

print('\n\tGross Profit:\n',gross_profit, '\n')
user_gross_profit =('us-gaap:' + input('Gross Profit: '))

print('\n\tTax:\n',tax, '\n')
user_taxes = 'us-gaap:' + input('Taxes: ')

print('\n\tSG&A:\n',sga, '\n')
user_sga = 'us-gaap:' + input('SG&A: ')

print('\n\tDepreciation:\n',dep, '\n')
user_dep = 'us-gaap:' + input('Depreciation: ')

print('\n\tAmortization:\n',amor, '\n')
user_amort = 'us-gaap:' + input('Amortization: ')

print('\n\tCurrent Assets:\n',ass_cur, '\n')
user_ass_cur = 'us-gaap:' + input('Current Assets: ')

print('\n\tCurrent Liabilities:\n',lia_cur, '\n')
user_lia_cur = 'us-gaap:' + input('Current Liabilities: ')

print('\n\tPPE:\n',ppe, '\n')
user_ppe = 'us-gaap:' + input('PPE')

print('\n\tInterest:\n',interest, '\n')
user_int = 'us-gaap:' + input('Interest')

print('\n\tLTD:\n',ltd, '\n')
user_ltd = 'us-gaap:' + input('LTD')

user_time = int(input('What is the starting year?'))

user_time_end = int(input('What is the ending year?'))

years = []
user_time_end = 2013
while user_time != user_time_end-1:
    years.append(user_time)
    user_time -= 1

master = {}
master[user_gross_profit] = {}
master[user_taxes] = {}
master[user_sga] = {}
master[user_dep] = {}
master[user_amort] = {}
master[user_ass_cur] = {}
master[user_lia_cur] = {}
master[user_ppe] = {}
master[user_int] = {}
master[user_ltd] = {}

for year in years:
    # Access page
    cik = stock
    type = '10-K'
    dateb = '20191101'

    # Obtain HTML for search page
    base_url = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={}&type={}&dateb={}"
    edgar_resp = requests.get(base_url.format(cik, type, dateb))
    edgar_str = edgar_resp.text

    # Find the document link
    doc_link = ''
    soup = BeautifulSoup(edgar_str, 'html.parser')
    table_tag = soup.find('table', class_='tableFile2')
    rows = table_tag.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
    #     print(cells)
        if len(cells) > 3:
            if str(year) in cells[3].text:
                doc_link = 'https://www.sec.gov' + cells[1].a['href']

    # Exit if document link couldn't be found
    if doc_link == '':
        print("Couldn't find the document link")
        sys.exit()

    # Obtain HTML for document page
    doc_resp = requests.get(doc_link)
    doc_str = doc_resp.text

    # Find the XBRL link
    xbrl_link = ''
    soup = BeautifulSoup(doc_str, 'html.parser')
    table_tag = soup.find('table', class_='tableFile', summary='Data Files')
    rows = table_tag.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        if len(cells) > 3:
            if 'INS' in cells[3].text:
                xbrl_link = 'https://www.sec.gov' + cells[2].a['href']

    # Obtain XBRL text from document
    xbrl_resp = requests.get(xbrl_link)
    xbrl_str = xbrl_resp.text
    
    # Find and print stockholder's equity
    soup = BeautifulSoup(xbrl_str, 'lxml')
    tag_list = soup.find_all([re.compile('us-gaap:')])
    gaap = [user_gross_profit, user_taxes, user_sga, user_dep, user_amort, user_ass_cur, user_lia_cur, user_ppe, user_int, user_ltd]

    
    
    for tag in tag_list:
        for item in gaap:
            if tag.name == item:
                if int(tag.text) > 0:
                    stuff = str(tag)
                    stuff = re.findall(r'.*([2][0][1][0-9])', stuff)
                    stuff = list(map(lambda x: x.strip('_'), stuff))
                    value = int(tag.text)/1000000
#                     if value not in master[tag.name][stuff[-1]].values():
                    master[tag.name][stuff[-1]] = value

df = pd.DataFrame(master)

rename_list = ['grossprofit', 'taxes', 'sga', 'depreciation', 'amortization', 'assets', 'liabilities', 'ppe', 'interest', 'ltd']
rename_dict = {}
count_rename = 0 
for x in master.keys():
    index = x
    rename_dict[index] = rename_list[count_rename]
    count_rename += 1

df = df.rename(columns=rename_dict)

years_1 = years[-1] - 1
years_2 = years[-1] -2
years.append(years_1)
years.append(years_2)

for index in df.index:
    if int(index) not in years:
        df = df.drop(index)
        
df = df.fillna((df.shift() + df.shift(-1)/2))
df = df.fillna(df.shift(1))
df = df.fillna(df.shift(-1))

df['capex'] = df['ppe'] - df['ppe'].shift(1) + df['depreciation']

df = df.fillna(df.min())

df['ltd_change'] = df['ltd'] - df['ltd'].shift(-1) 

df['ebit'] = df['grossprofit'] - df['depreciation'] - df['sga']

df['nopat'] =  df['ebit'] - df['taxes']

df['ocf'] = df['nopat'] + df['depreciation']

df['current_working_capital'] = df['assets'] - df['liabilities']

df['change_nwc'] = -(df['current_working_capital'] - df['current_working_capital'].shift(1))

df = df.apply(lambda x: x.fillna( (x.mean()),axis=0))

df['fcff'] = df['ocf'] - df['capex']  - df['change_nwc']

print(df[['fcff']].T)