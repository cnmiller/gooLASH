#Google Lightweight Search Hacking (gooLASH)
#Written by Chase Miller (@psuchase)
#Secquity.com

from lxml import html
import requests

#Retrieve the exploit-db.com Google Hacking Database (GHDB)
page = requests.get('https://www.exploit-db.com/google-hacking-database/')
tree = html.fromstring(page.content)
