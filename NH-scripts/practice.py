import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import numpy as np

#col_list=[Name,Ref,tag]


headers = {
    'authority': 'tools.kali.org',
    'method': 'GET',
    #'path': '/information-gathering/ace-voip',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'referer': 'https://tools.kali.org/tools-listing',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
}

df = pd.read_csv("kali-list.csv", usecols=[1])
url_brackets = np.array(df)
url = str(url_brackets[0])[2:-2]
print(str(url))
print('making requests...')
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.p.text) 
time.sleep(2)

# #url = url_list[1]
# print('making requests...')
# page = requests.get(url, headers=headers)
# soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.find('h2').text)
# time.sleep(2)


# for url in url_list:
#     try:
#         print('making requests...')
#         page = requests.get(url, headers=headers)
#         soup = BeautifulSoup(page.content, 'html.parser')
#         print(soup.find('h2').text)
#         time.sleep(2)
#     except:
#         print('request not made')