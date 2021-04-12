import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import numpy as np


col_list=['description']


headers = {
    'authority': 'tools.kali.org',
    'method': 'GET',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'referer': 'https://tools.kali.org/tools-listing',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 8.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0',
}

array = []

df = pd.read_csv("kali-links.csv", usecols=[0])
url_list = df.values.tolist()

for i in range(1,len(url_list)):
    if i%5 == 0:
        print('saving to csv')
        array = np.array(array)
        pd.DataFrame(array).to_csv("kali-list copy.csv", mode='a', header=False, index=False) # ({'description': array})
        # df2 = df2.astype({'description': object})
        # df2.to_csv("NH-scripts\\kali-list copy.csv", mode='a', header=False, index=False)
        array = []
        print('continuing')
        continue
    try:
        url = np.array(df)
        url = str(url[i])[2:-2]
        print('making requests...')
        print(str(url))
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        desc = soup.p.text
        array.append([url.rsplit('/', 1)[-1], desc])
        time.sleep(1)
    except:
        array.append([url.rsplit('/', 1)[-1], 'request failed'])
    i+=1

pd.DataFrame(array).to_csv("kali-list copy.csv", mode='a', header=False, index=False)
# df = pd.DataFrame({'description': array})
# df = df.astype({'description': object})
# df.to_csv("NH-scripts\\kali-list copy.csv", mode='a', header=False, index=False)