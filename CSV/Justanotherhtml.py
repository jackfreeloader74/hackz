import requests
from bs4 import BeautifulSoup

header = {
'authority': 'cyberarch.eu',
'path': '/red-teaming-adversary-simulation-toolkit/',
'scheme': 'https',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'cache-control': 'max-age=0',
'cookie': '__cfduid=d3ceef5ddf21bc16f700bffc1de6ca6241618605608; PHPSESSID=468e4e18ccba36364cb69d2142867016; cookielawinfo-checkbox-necessary=yes; cookielawinfo-checkbox-non-necessary=yes; CookieLawInfoConsent=eyJuZWNlc3NhcnkiOnRydWUsIm5vbi1uZWNlc3NhcnkiOnRydWV9; viewed_cookie_policy=yes',
'referer': 'https://www.google.com/',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
}
page = requests.get('https://cyberarch.eu/red-teaming-adversary-simulation-toolkit/', headers=header).text
soup = BeautifulSoup(page, 'html.parser')
f = open('redteamtools.html', 'w')
f.write(soup.prettify())
f.close()
