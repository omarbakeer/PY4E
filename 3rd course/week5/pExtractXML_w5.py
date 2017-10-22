import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


url = input('Enter URL: ')
data = urllib.request.urlopen(url).read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)
results = tree.findall('.//count')
total = 0
for item in results :
    total = total + int(item.text)
print(total)