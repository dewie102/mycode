#!/usr/bin/env python3

import time
import os

def main():
    user_input = input("Please enter the number of beers on the wall: ").strip()
    try:
        beers = int(user_input)
        if(beers > 100 or beers < 1):
            print("Please choose a number between 1 and 100") 
    except:
        print("Next time please enter a proper number...")
        return

    for count in range(beers, 0, -1):
        os.system("clear")
        print(f"{count} bottles of beer on the wall!")
        time.sleep(1)
        print(f"{count} bottles of beer on the wall! {count} bottles of beer! You take one down, pass it around!")
        time.sleep(2)

    print("No more bottles of beer on the wall.... time to go home")

if __name__ == "__main__":
    main()
