# eu_scraper

How to (more or less):
1. download the script
2. install python3
3. cd terminal to file location
4. pip install -r requirements.txt
5. go to eu-website, check how many sites are available, and change range in line 44 to that+1
   e.g. 200 available -> "range(1, 201)"
6. copy "ASPXAUTH" Cookie after "=" to line 9
-> press F12 in browser, switch to network, click on any entry, look for your cookies and copy anything after ".ASPXAUTH=" to line 9

run the script :p
