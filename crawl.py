import urllib
import urllib.request, urllib.error, urllib.parse
from urllib.request import Request, urlopen
import ssl
import re
import requests
from bs4 import BeautifulSoup as bs
import os

directory = 'spring'
if not os.path.exists(directory):
	os.makedirs(directory)
	
url = input("Enter the url: ")

# url = "https://wallhaven.cc/search?tags=car"
	
req = Request(url, headers = {'User-Agent':'Mozilla/5.0'})
html = urllib.request.urlopen(req).read()
sop = bs(html, 'html.parser')

tags = sop('img')

def checkvalidImageUrl(imageUrl):
	return (imageUrl is None or len(imageUrl) <= 3 or len(re.findall('^.*\.(jpg|JPG|gif|GIF|png|PNG|jpeg|JPEG)$',imageUrl))!=1) 
	
counter = 0
for each_tag in tags:
	imgs = each_tag.get('src', None)
	dataimgs = each_tag.get('data-src',None)
	
	if checkvalidImageUrl(imgs):
		if checkvalidImageUrl(dataimgs):
			continue
		else:
			del(imgs)
			imgs = dataimgs
			
	type1 = [] #local addresses
	type2 = [] 
	t1 = re.findall('^//', imgs)
	if len(t1) > 0:
		type1 = 1
	else:
		t2 = re.findall('http',imgs)
		if len(t2) == 0:
			type2 = 1
			
	opener = urllib.request.build_opener()
	opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
	urllib.request.install_opener(opener)
	
	if type1 == 1:
		imgs = "https:"+imgs
	elif type2 == 1:
		if imgs[0] == '/':
			imgs = url + imgs
		else:
			imgs = url + '/' + imgs
	lastcheck = re.findall(".*\.\..*", imgs)
	if len(lastcheck) >= 1:
		continue;
	print(imgs)
	
	try:
		urllib.request.urlretrieve(imgs, 'spring/' + str(counter) + '.jpg')
	except:
		continue;
	else:
		counter+=1;
		
print("program was successful")

