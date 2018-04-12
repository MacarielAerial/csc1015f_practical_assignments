# This program prints out every 7th number starting from the number inputed up until 41 numbers after the inputed number
# Student Name: Yifei Yu
# Course Code: CSC1015F
# Date: 21th March 2018

# Request input
n = eval(input("Enter a number: "))

# Evaluate validity
if -6<n<2:
	for every7th_number in range(n,n+41,7):
		print("{0:>2}".format(every7th_number), end="\n")
