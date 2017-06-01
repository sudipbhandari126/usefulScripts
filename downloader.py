import requests
from bs4 import BeautifulSoup as bs
import urllib2
import os


_URL = 'http://advancedlinuxprogramming.com/alp-folder/'

# functional
r = requests.get(_URL)
soup = bs(r.text)
urls = []
names = []
for i, link in enumerate(soup.findAll('a')):
    _FULLURL = _URL + link.get('href')
    if _FULLURL.endswith('.pdf'):
        urls.append(_FULLURL)
        names.append(soup.select('a')[i].attrs['href'])

names_urls = zip(names, urls)

for name, url in names_urls:
    print url
    cmd = 'wget {0}'.format(url)
    print cmd
    os.system(cmd)