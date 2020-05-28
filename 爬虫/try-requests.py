import requests
import re
from bs4 import BeautifulSoup

url = 'http://www.cntour.cn/'

#设置请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0",
    "Cookie": "_bfa=1.1590570896388.2pkfvl.1.1590570896388.1590570896388.1.4; _bfs=1.4; _RF1=111.194.44.11; _RSG=G04OaDnd746ezTAHPvcpeB; _RDG=280e472ac690a52a352a4f7b2148ce114f; _RGUID=61079f13-6460-4010-ba33-9b965129df68; _bfi=p1%3D0%26p2%3D0%26v1%3D4%26v2%3D0"
}

# 发送请求
strhtml = requests.get(url,headers=headers)

# 获取标签数据
soup = BeautifulSoup(strhtml.text, 'lxml')
data = soup.select('div.mtop:nth-child(4) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li > a')
print(data)

# 遍历 获取标签的内容
for item in data:
    result = {
        'title': item.get("title"),
        'link': item.get('href'),
        'ID': re.findall('\d+', item.get('href'))
    }
    print(result)