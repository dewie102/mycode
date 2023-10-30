#!/usr/bin/env python3


def main():
    name = input("Please enter your name: ")
    day_of_week = input("What day of the week is it? ")

    print("Hello, {}! Happy {}!".format(name, day_of_week))

if __name__ == "__main__": # detects if the code is being imported or being run directly
    main();
