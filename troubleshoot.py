#!/usr/bin/env python3

def main():
    user_input = input("Enter some words separated by spaces: ")
    words = user_input.split(" ")

    print("Splitting the words:")
    print(words)

    joined_words = "-".join(words)
    print("Joining the words with hyphens:")
    print(joined_words)

main()
