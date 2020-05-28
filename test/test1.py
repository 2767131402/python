from lxml import etree
from bs4 import BeautifulSoup


wb_data = """
        <div>
            <ul>
                 <li class="item-0"><a href="link1.html">first item</a></li>
                 <li class="item-1"><a href="link2.html">second item</a></li>
                 <li class="item-inactive"><a href="link3.html">third item</a></li>
                 <li class="item-1"><a href="link4.html">fourth item</a></li>
                 <li class="item-0"><a href="link5.html">fifth item</a>
             </ul>
         </div>
"""
bs = BeautifulSoup(wb_data, 'lxml')
texts = bs.find('div')
print(texts)
uls = texts.find("ul")
print(uls)
lis = uls.find_all("li")
print(lis)