import urllib.request
import json

url="http://api.open-notify.org/astros.json"

response = urllib.request.urlopen(url)

scraped = response.read()

workingstring = scraped.decode("utf-8")

jsondata= json.loads(workingstring)

print(workingstring)
print(type(jsondata))
print(jsondata["number"])
