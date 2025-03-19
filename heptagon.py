#!/usr/bin/env python3
"""
Created by: Janet Do 
Created on: Mar 2025 
This is the area of a heptagon
"""
import math

def main():
    """The main() function calculates the perimeter of a pentagon, returns None."""
    # input
    length = int(input("Enter side length of the heptagon (cm): "))

    # process
    area = 1.75* length**2* (1/math.tan(math.pi/7))

    # output
    print(f"The area is: {area:.2f} cm2.")
    print("\nDone.")


if __name__ == "__main__":
    main()
