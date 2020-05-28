from bs4 import BeautifulSoup
import requests

target = 'https://www.biqukan.com/1_1094/'
req = requests.get(url=target)
req.encoding="gbk"
bf = BeautifulSoup(req.text,"lxml")
# texts = bf.find_all('div', id='content')
data = bf.select(".listmain > dl > dd > a")
for item in data:
    result = {
        'title': item.get_text(),
        'href':item.get("href")
    }
    print(result)
