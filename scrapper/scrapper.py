
from ntpath import join
from unicodedata import category
from bs4 import BeautifulSoup
import requests
from scrapper.formatter import *
import json


# http://www.imadislam.com/hisnulmuslim/

# print(soup.prettify())

## for i in range (1,133):
with open("azkar.json","w",encoding="utf-8") as test:
    azkar_dict={}
    categories_list=[]
    for i in range(1,133):
        response = requests.get('http://www.imadislam.com/hisnulmuslim/'+formatNumber(i) + ".htm")
        soup  = BeautifulSoup(response.content,"html.parser")
        azkar = soup.select("td > p")
        azkar.pop(0)
        azkar.pop(0)
        category = azkar[0].text
        categories_list.append(category)
        printa(category)
        azkar.pop(0)
        zekrs = []
        for i in azkar:
            zekr_dict = {"category":category,"content": i.text}
            zekrs.append(zekr_dict)
            # printa(i.text.strip())
            # test.write(i.text.strip())
        azkar_dict[category] = zekrs
    data = json.dumps(azkar_dict,indent=2,ensure_ascii=False)
    test.write(data)
    print(categories_list)
    file = open("test.txt","w",encoding="utf-8")
    file.write(str(categories_list))
