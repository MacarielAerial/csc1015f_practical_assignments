# This program prints out a text based graph of function f(x)

import math
function = input("Enter a function f(x):\n")
for y in range(10, -11, -1):
	for x in range(-10, 11):
		result = round(eval(function))
		if result == y:
			print("*", end="")
		elif x == 0 and y == 0:
			print("+", end="")
		elif y == 0:
			print("-", end="")
		elif x == 0:
			print("|", end="")
		else:
			print(" ", end="")
	print()
