#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()


        character_name = got_dj["name"]
        if not character_name:
            character_name = got_dj["aliases"][0]

        books = got_dj["books"]
        book_names = []
        for book in books:
            bookresp = requests.get(book)
            book_names.append(bookresp.json()["name"])

        allegiances = got_dj["allegiances"]
        allegiance_names = []
        for allegiance in allegiances:
            allegresp = requests.get(allegiance)
            allegiance_names.append(allegresp.json()["name"])

        
        print(character_name)
        print("books:")
        print(f'\t{str.join(", ", book_names)}')
        print("Allegiances: ")
        print(f'\t{str.join(", ", allegiance_names)}')


        #pprint.pprint(got_dj)

if __name__ == "__main__":
        main()

