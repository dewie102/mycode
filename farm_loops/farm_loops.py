#!/usr/bin/env python3


farms = [{"name": "Southwest Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "Northeast Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "East Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]}]


plants = ["carrots", "celery", "bananas", "apples", "oranges"]

def main():
    for farm in farms:
        print("-", farm["name"])
    choice= input("Pick a farm!\n")

    for farm in farms:
        if farm["name"].lower() == choice.lower():
            for animal in farm["agriculture"]:
                if animal not in plants:
                    print(animal)


if __name__ == "__main__":
    main()
