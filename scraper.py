from email import header
from urllib.request import Request
import requests
from pprint import pprint
url = "https://espirs.jrc.ec.europa.eu/en/espirs/public/publicview/1e7dc743-971e-400c-b2d6-275a8bb65690" 

cookies_dict = {'.ASPXAUTH' : ""}

r = requests.get(url=url, cookies=cookies_dict)

pprint(r.text)