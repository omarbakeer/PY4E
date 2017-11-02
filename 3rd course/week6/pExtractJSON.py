import urllib.request, urllib.parse, urllib.error
import json

url = input("Enter location: ")
print('Retrieving', url)
connection = urllib.request.urlopen(url)
data = connection.read().decode()
print('Retrieved', len(data), 'characters')

info = json.loads(data)

total = 0
for item in info["comments"]:
    total = total + int(item['count'])
print("Sum =",total)
