from urllib.request import urlopen
from urllib import parse
from urllib import request
from bs4 import BeautifulSoup
import requests
from requests.utils import requote_uri
import re

keyword = input("search:")
url = "https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=" + keyword
U = requote_uri(url)
page = urlopen(U)
content = page.read().decode("utf-8")
soup =  BeautifulSoup(content, 'html.parser')
for a in soup.find_all('a', text = re.compile('CVE-')):
	b = a.text.replace("None","")
	print(b)
#for CVSS in soup.find_all('td', text = re.compile('Base Score')):
#	c = CVSS.text
#	print(b,":",c)
#	CVSS.next_sibling 
