import requests
# 3rd party! MOST POPULAR python library out there for HTTP requests

url = "https://anapioficeandfire.com/api/books/1"

response = requests.get(url) # GET requests are the most common
        #.post()
        #.put()
        #.delete()
        # for every HTTP request there is, there is a matching function

#jsondata = response.text
jsondata = response.json()

print(type(jsondata))
print(jsondata["authors"])
