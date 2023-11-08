#!/usr/bin/env python3

import requests

POSTURL = "https://petstore.swagger.io/v2/pet"

def main():
    mydata = {
      "id": 50,
      "category": {
        "id": 0,
        "name": "string"
      },
      "name": "doggie",
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 0,
          "name": "string"
        }
      ],
      "status": "available"
    }

    resp = requests.post(POSTURL, json=mydata, timeout=10)

    print(resp.json())

if __name__ == "__main__":
    main()
