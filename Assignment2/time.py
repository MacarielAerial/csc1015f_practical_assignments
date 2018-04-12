# This program is for checking the validity of a time entered by the user as a set of three integers
# CSC1015F Assignment1 Question Number 3
# Name: Yifei Yu
# Date: 8th March 2018

# Request input numbers from the user
hours = eval(input("Enter the hours: "))
minutes = eval(input("Enter the minutes: "))
seconds = eval(input("Enter the seconds: "))

# Check if these input numbers are valid
if 0 <= hours <= 23:
	valid_h = 1
else:
	valid_h = 0
if 0 <= minutes <= 59:
	valid_m = 1
else:
	valid_m = 0
if 0 <= seconds <= 59:
	valid_s = 1
else:
	valid_s = 0

# Check if all three criterions are met and print out the result
if valid_h == 1 and valid_m == 1 and valid_s == 1:
	print("Your time is valid.")
else:
	print("Your time is invalid.")
