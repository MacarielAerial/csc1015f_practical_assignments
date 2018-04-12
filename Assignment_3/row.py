# The program is to print a sequence of 7 numbers that started with the value that user entered
# Student Name: Yifei Yu
# Course Code: CSC1015F
# Assignment 3

# Request input from users
n = eval(input("Enter the start number: "))

# Evaluate input validity
if -6 <n<93:
	for sequence in range(n,n+7):
		print("{0:>2}".format(sequence), end=" ")
print()
