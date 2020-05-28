import requests
from bs4 import BeautifulSoup

url = "https://unsplash.com/"

resp = requests.get(url=url)
# html = etree.HTML(resp.text)
# # html_data = html.xpath('/html/body/div/div/div[4]/div[2]/div[1]/div/div')
# html_data = html.xpath('/html/body/div/div/div[4]/div[2]/div[1]/div/div/div[1]/div')
# print(html_data)
#
# for i in html_data:
#     print(i.text)
soup = BeautifulSoup(resp.text, 'lxml')
data = soup.select(".qztBA > div > div > figure > a")
print(len(data))
for item in data:
    # print(type(item))
    print(item)
    # a = {
    #     'href':item.get('href')
    # }
    # print(a)
