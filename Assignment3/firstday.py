# This program asks the user to enter a year range and that prints out the name of the day on which the 1st of January falls for each year in that range.
# Name: Yifei Yu
# Date: 16th March 2018
# Course: CSC1015F

first_year = eval(input("Enter the first year:\n"))
second_year = eval(input("Enter the second year:\n"))

for year in range(first_year, second_year + 1):
	day = 5 * ((year - 1) % 4)	
	day = 1 + day + 4 * ((year - 1) % 100)
	day = day + 6 * ((year - 1) % 400)
	day = day % 7
	if day == 0:
		print("The 1st of January", year, "falls on a Sunday.")
	if day == 1:
		print("The 1st of January", year, "falls on a Monday.")
	if day == 2:
		print("The 1st of January", year, "falls on a Tuesday.")
	if day == 3:
		print("The 1st of January", year, "falls on a Wednesday.")
	if day == 4:
		print("The 1st of January", year, "falls on a Thursday.")
	if day == 5:
		print("The 1st of January", year, "falls on a Friday.")
	if day == 6:
		print("The 1st of January", year, "falls on a Saturday.")
