#!/usr/bin/env python3

# Created by Wenda Zhao
# Created on Nov 2020
# This program calculates the circumference of a circle
#     with user input

import constants


def main():
    # This function calculates circumference

    # input
    radius = int(input("Enter radius of the circle (mm): "))

    # process
    circumference = constants.TAU*radius

    # output
    print("")
    print("Circumference is {}mm²".format(circumference))


if __name__ == "__main__":
    main()
