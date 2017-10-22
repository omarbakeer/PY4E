# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
counter = int(input('Enter count: '))
position = int(input('Enter position: '))

while counter >= 0 :
	print('Retrieving:',url)
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')

	# Retrieve all of the anchor tags
	tags = soup('a')
	pos = 1
	for tag in tags :
		if pos == position :
			url = tag.get('href', None)
			break
		else :
			pos = pos + 1
	counter = counter - 1

