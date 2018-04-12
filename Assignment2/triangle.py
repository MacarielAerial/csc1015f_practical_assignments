# CSC1015F Assignment 1 Question Number 4
# Name: Yifei Yu
# Student ID: YXXYIF001
# Date: 8th March 2018

# Import maths library
import math

# Request input of lengths of three sides of a triangle from the user
first_side = eval(input("Enter the length of the first side: "))
second_side = eval(input("Enter the length of the second side: "))
third_side = eval(input("Enter the length of the third side: "))

# Calculate the area of the triangle and export the result
circumference = (first_side + second_side + third_side)/2
area = math.sqrt(circumference*(circumference - first_side)*(circumference - second_side)*(circumference - third_side))
print("The area of the triangle with sides of length", first_side, "and", second_side, "and", third_side, "is", area, end=".")
