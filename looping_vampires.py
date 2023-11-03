#!/usr/bin/env python3

def main():
    count = 0
    filename = "lineswithvampire.txt"

    outfile = open(filename, "a")

    with open("dracula.txt", "r") as infile:
        for line in infile:
            if("vampire" in line.lower()):
                print(line, end="")
                count += 1
                outfile.write(line)

    print(f"'Vampire' appears {count} times")
    outfile.close()


if __name__ == "__main__":
    main()
