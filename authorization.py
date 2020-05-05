import requests
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import webbrowser


url = 'https://grouple.co'
login = 'DRAGON SCALE'
password = '01k7fc31dkw'
s = requests.Session()
r = s.get(url, auth=(login, password))

 
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print('URL:', tag.get('href', None))
   