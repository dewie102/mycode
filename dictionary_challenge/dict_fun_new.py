#!/usr/bin/env python3

import json
import os


def main_menu():
    valid_choice = False
    choice = ""
    while(not valid_choice):
        print("Please choose one of the following options")
        print("1. List keys in dictionary")
        print("2. View the value of a specific key")
        print("3. Add a key value pair to the dictionary")
        print("q. to quit")
        choice = input("> ")

        if(not choice.isdigit() and choice == "q"):
            valid_choice = True
        elif(choice.isdigit() and (choice == "1" or choice == "2" or choice == "3")):
            valid_choice = True
        else:
            os.system("clear")
            print("invalid choice, please try again")
            print()
            continue

    return choice


def list_dictionary_keys(dict):
    print("The dictionary has the following keys to choose from: ")
    print(dict.keys())
    print()


def get_key_from_user(dict):
    valid_input = False
    key = ""
    while(not valid_input):
        key = input("Please enter a key you want to see the value of: ")
        if dict.get(key) is None:
            os.system("clear")
            print(f"You entered an invalid key: {key}")
            print()
            continue

        valid_input = True
    
    return key


def print_key_value(dict, key):
    print(f"The value for key {key} is: {dict[key]}")
    print()


def get_new_value_from_user(prompt):
    value = input(prompt)
    return value


def add_key_pair_to_dict(dict, key, value):
    dict[key] = value


def main():
    with open('dictionary.dict') as f:
        data = f.read()

    dict = json.loads(data)

    print("imported dictionary: ")
    print(dict)
    print()

    while True:
        choice = main_menu()

        if(choice == "q"):
            return
        
        os.system("clear")
        if(choice == "1"):
            list_dictionary_keys(dict)
        elif(choice == "2"):
            list_dictionary_keys(dict)
            key = get_key_from_user(dict)
            print_key_value(dict, key)
        elif(choice == "3"):
            key = get_new_value_from_user("Please enter a key for the dictionary: ")
            value = get_new_value_from_user("Please enter a value for the dictionary: ")
            add_key_pair_to_dict(dict, key, value)
            os.system("clear")
    

if __name__ == "__main__":
    main()
