#!/usr/bin/python3

import requests

# define the URL we want to use
IPURL = "https://petstore.swagger.io/v2/pet/findByStatus?status=available"

def main():
    # use requests library to send an HTTP GET
    resp = requests.get(IPURL)

    # strip off JSON response
    # and convert to PYTHONIC LIST / DICT
    respjson = resp.json()

    # display our PYTHONIC data (LIST / DICT)
    print(respjson)

if __name__ == "__main__":
    main()

