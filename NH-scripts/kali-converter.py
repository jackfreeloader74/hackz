# from bs4 import BeautifulSoup
# import pandas as pd
# import urllib.request

# col_names = ['tool name', 'tool ref']

html_doc = urllib.request.urlopen("https://tools.kali.org/tools-listing")
with open(html_doc) as csvfile:
    soup = BeautifulSoup(csvfile, 'html.parser')

# array = []
# href = []
# title = []
# for link in soup.find_all('a'):
#     df = pd.DataFrame({'name': [link.get('title')], 'ref': [link.get('href')], 'h-name': [link.get('href').rsplit('/', 1)[-1]], 'category': [link.get('href').rsplit('/', 2)[-2]]})
#     df.to_csv('kali-list.csv', mode='a', header=False, index=False)

