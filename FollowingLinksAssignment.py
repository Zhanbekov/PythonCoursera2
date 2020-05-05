import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

count = 8
pos = 17
url_list=list()

for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags=soup('a')
    print('Retrieveing:',url)
    taglist=list()
    for tag in tags:
        x=tag.get('href',None)
        taglist.append(x)

    url=taglist[pos]

    url_list.append(url)

print("Last Url:",url_list[-2])
