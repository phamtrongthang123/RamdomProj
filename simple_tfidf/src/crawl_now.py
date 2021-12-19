import requests
import bs4
from rich import print
import json 
from utils import *

text= "abstract algebra research"
url = 'https://google.com/search?q=' + text
  
request_result=requests.get( url )
soup = bs4.BeautifulSoup(request_result.text,
                         "lxml")

heading_object=soup.find_all( 'div', class_="BNeawe s3v9rd AP7Wnd" )

data_set = set()
for info in heading_object:
    data_set.add(info.getText())

data_list = []
for item in data_set:
    item = tokenize(item)
    data_list.append(item)

with open("data_19.12.2021.json", "w", encoding="utf-8") as f:
    json.dump(data_list, f, ensure_ascii=False)

