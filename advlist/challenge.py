#!/usr/bin/env python3

import random

def main():
    wordbank= ["indentation", "spaces"] 
    tlgstudents=["Bert", "Angel", "Chandan", "Chris", "Gen", "Jojo", "Joseph", "Robert", "Sar", "Zack"]

    wordbank.append(4)

    max_number = len(tlgstudents)

    num_str = input(f"Please enter a number from 1 to {max_number}: ")

    try:
        num = int(num_str) - 1
    except ValueError:
        print("Please enter a proper number")
        return;

    if 0 > num or num > max_number - 1:
        print("Pick a number inside the proper range")
        return;

    random.shuffle(tlgstudents)

    student_name = tlgstudents[num]

    print(f"{student_name} always uses {wordbank[-1]} {wordbank[1]} to indent.")

if __name__ == "__main__":
    main()
