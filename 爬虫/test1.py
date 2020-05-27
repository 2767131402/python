import requests
import re
from bs4 import BeautifulSoup

url = 'http://www.cntour.cn/'
strhtml = requests.get(url)

soup = BeautifulSoup(strhtml.text, 'lxml')
data = soup.select('div.mtop:nth-child(4) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li > a')
print(data)

for item in data:
    result = {
        'title': item.get("title"),
        'link': item.get('href'),
        'ID': re.findall('\d+', item.get('href'))
    }
    print(result)