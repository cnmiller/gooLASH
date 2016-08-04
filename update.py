#Google Lightweight Automated Search Hacking (gooLASH)
#Written by Chase Miller (@psuchase)

import urllib2
import requests
from BeautifulSoup import BeautifulSoup
# or if you're using BeautifulSoup4:
# from bs4 import BeautifulSoup

soup = BeautifulSoup(requests.get('https://www.exploit-db.com/google-hacking-database/', verify=False).text)

for row in soup('table'):
    tds = row('td')
    print tds[0].string, tds[1].string
    # will print date and sunrise