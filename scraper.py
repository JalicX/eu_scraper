from email import header
from urllib.request import Request
import requests
from bs4 import BeautifulSoup
import requests
import json
import os

def dump(data:dict, folder:str='tmp', filename:str='dump'):
    if not os.path.isdir(folder):
        os.mkdir(folder)
    with open(f"{folder}/{filename}.json", 'w') as file:
        json.dump(data, file, indent=4)

url = "https://espirs.jrc.ec.europa.eu/en/espirs/public/publicview/1e7dc743-971e-400c-b2d6-275a8bb65690" 

cookies_dict = {'.ASPXAUTH' : ""}

r = requests.get(url=url, cookies=cookies_dict)

soup = BeautifulSoup(r.content, 'html.parser')

#print(soup.prettify)

matches = soup.findAll('div', class_='r')

data = dict()

for match in matches:
    d = match.find('div', class_='lbl')
    e = match.find('div', class_='val')
    if d is None or e is None:
        continue
    try:
        data[d.text] = e.text
    except:
        print(f"Ploblemo with: {d}, {e}")


dump(data)
#print(data)
