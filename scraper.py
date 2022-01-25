from bs4 import BeautifulSoup
import requests
import json
import os


baseurl = "https://espirs.jrc.ec.europa.eu" 

cookies_dict = {'.ASPXAUTH' : ""}



def dump(data:dict, folder:str='tmp', filename:str='dump'):
    if not os.path.isdir(folder):
        os.mkdir(folder)
    with open(f"{folder}/{filename}.json", 'w') as file:
        json.dump(data, file, indent=4)

def get_one_object(path:str):
    
    url     = baseurl + path
    r       = requests.get(url=url, cookies=cookies_dict)
    soup    = BeautifulSoup(r.content, 'html.parser')
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
    
    del url, r, soup, matches
    return data

def main():
    # TODO : Get List of paths
    paths = ["1e7dc743-971e-400c-b2d6-275a8bb65690"]

    allObjects = list()

    for path in paths:
        allObjects.append(get_one_object(path))

    dump(allObjects)

def get_paths_of_page(page:int):
    result = []
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0"}
    nurl     = f"https://espirs.jrc.ec.europa.eu/en/espirs/public/PublicSearchResults?searchingtext=&status=&seveso=&industrytype=&country=&currentPage={page}&rpp=10&nace=&sortby=&sortdir=ASC"
    r       = requests.get(url=nurl, cookies=cookies_dict, headers=headers)
    soup    = BeautifulSoup(r.content, 'html.parser')
    #print(soup.prettify) 
    list = soup.find('ol')
    matches = list.findAll('a', class_="title")
    for idx, match in enumerate(matches, start=1):
        result.append(match['href'])
    return result

if __name__ == "__main__":
    main()
