from pip._vendor import requests
from bs4 import BeautifulSoup
import pandas as pd

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
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
}

url_list = pd.read_csv("kali-list.csv", usecols=[1])
for url in url_list:
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup.find('h2').text)
