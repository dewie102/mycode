#!/usr/bin/env python3

import json

def main():
    # reading the data from the file
    with open('dictionary.dict') as f:
        data = f.read()

    # reconstructing the data as a dictionary
    dict = json.loads(data)

    print("imported dictionary: ")
    print(dict)
    print()

    print("The dictionary has the following keys to choose from: ")
    print(dict.keys())

    key = input("Please enter a key you want to see the value of: ")
    if dict.get(key) is None:
        print(f"You entered an invalid key: {key}")
        return;

    print(f"The value for key {key} is: {dict[key]}")

    answer = input("Would you like to input any data? [y/N]")

    if answer == "y" or answer == "Y":
        new_key = input("please enter new key: ")
        new_value = input("Please enter new value: ")
        dict[new_key] = new_value;
    else:
        print("Cool")
        return;

    print(dict)


if __name__ == "__main__":
    main()
