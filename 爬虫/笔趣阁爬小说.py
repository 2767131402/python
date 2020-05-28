import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = 'https://www.xsbiquge.com/15_15338/8549128.html'
    req = requests.get(url = url)
    req.encoding = 'utf-8'
    
    bs = BeautifulSoup(req.text, 'lxml')
    texts = bs.find('div', id='content')
    # 去掉 换行符
    print(texts.text.strip().split('\xa0'*4))
