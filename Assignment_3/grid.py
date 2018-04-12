# This program prints out 6 rows of 7 numbers that contain values of n and n+41
# Student Name: Yifei Yu
# Course Code: CSC1015F
# Assignment 3

# Request input
n = eval(input("Enter the start number: "))

# Evaluate validity and print out results
if -6 < n < 2:
	for row in range(0,6):
		for column in range(0,7):
			print("{0:>2}".format(column + (row * 7) + n), end = " ")
		print("\n", end = "")
