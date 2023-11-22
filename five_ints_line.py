#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: November 21, 2023
# This program displays all numbers between 1000 and 2000, but there is a newline for every multiple of 5


def main():
    # show what the program does
    print(
        "This program displays all numbers between 1000 and 2000, but there is a newline for every multiple of 5."
    )

    # initialize counter to 1
    counter = 1

    # use a for loop for all numbers between 1000 and 200
    for counter in range(1000, 2001, 1):
        # if the counter is 1000, print counter on the same line
        if counter == 1000:
            print("{} ".format(counter), end="")
        elif counter % 5 == 0:
            # otherwise, if counter is a multiple of 5, create a newline
            print("\n{} ".format(counter), end="")
        else:
            # otherwise, print counter on the same line
            print("{} ".format(counter), end="")


if __name__ == "__main__":
    main()
