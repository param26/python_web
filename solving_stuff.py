# things to note:
	# make sure you have all the modules
	# make a folder named spring(see line 55) in which the images will get downloaded
	# type the correct url(along with http or https)
	# right now this can only surf the main page(depth of 1)
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

# some good wallpaper sites are:
	# https://www.walllhaven.cc
	# https://www.hdwallpapers.in
	
req = Request(url, headers = {'User-Agent':'Mozilla/5.0'})
html = urllib.request.urlopen(req).read()
sop = bs(html, 'html.parser')

tags = sop('img')
# print(tags)
counter = 0
for each_tag in tags:
	imgs = each_tag.get('src', None)
	if imgs == None or len(imgs) < 3 or len(re.findall('^.*\.(jpg|JPG|gif|GIF|png|PNG|jpeg|JPEG)$',imgs)) == 0:
		continue
	type1 = [] #local address, we will combine parent address and image address/ kind of like on http://www.google.com
	type2 = [] #improper addressing, like some on  https://www.wallhaven.cc
	t1 = re.findall('^//', imgs)
	if len(t1) > 0:
		type1 = 1
	else:
		t2 = re.findall('http',imgs)
		if len(t2) == 0:
			type2 = 1
	# print("img ",imgs)
	#useless stuff
	# if imgs[0] == '/'
	# if needFullUrl == 1:
		# url = url + imgs
		# req = Request(url, headers = {'User-Agent':'Mozilla/5.0'})
		# req = url
		# filename = str(counter) + '.jpg'
		# urllib.request.URLopener.urlretrieve(req, 'spring/dd.jpg')
	# else: 
		# url = imgs
		# req = Request(url, headers = {'User-Agent':'Mozilla/5.0'})
		# urllib.request.urlretrieve(url, 'spring/justdid.jpg')
	# counter+=1
	opener = urllib.request.build_opener()
	opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
	urllib.request.install_opener(opener)
	if type1 == 1:
		imgs = "https:"+imgs
		# print("img made ", imgs)
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
		urllib.request.urlretrieve(imgs, 'spring/' + str(counter) + '.jpg') #spring is the folder(can rename)
	except:
		continue;
	else:
		counter+=1;
print("program was successful")


# todo
# implement lazy load data-src
# set depth
