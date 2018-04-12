# This program prints out a calendar of the month specified by the user given that the user provides the starting day of the month
# Student Name: Yifei Yu
# Course Code: CSC1015F
# Assignment 3

# Ask for input of the month and the start day
month = input("Enter the month ('January', ..., 'December'): ") 
start_day = input("Enter the start day ('Monday', ..., 'Sunday'): ")




# Convert input string into numerical values
if start_day == "Monday":
	first_day = 1
elif start_day == "Tuesday":
	first_day = 0
elif start_day == "Wednesday":
	first_day = -1
elif start_day == "Thursday":
	first_day = -2
elif start_day == "Friday":
	first_day = -3
elif start_day == "Saturday":
	first_day = -4
elif start_day == "Sunday":
	first_day = -5

if month == "January":
	number_of_days = 31
elif month == "February":
	number_of_days = 28
elif month == "March":
	number_of_days = 31
elif month == "April":
	number_of_days = 30
elif month == "May":
	number_of_days = 31
elif month == "June":
	number_of_days = 30
elif month == "July":
	number_of_days = 31
elif month == "August":
	number_of_days = 31
elif month == "September":
	number_of_days = 30
elif month == "October":
	number_of_days = 31
elif month == "November":
	number_of_days = 30
elif month == "December":
	number_of_days = 31

# Print out results
print(month)
print("Mo Tu We Th Fr Sa Su")
for day in range(first_day,first_day + 42):
	if day <= 0 or day > number_of_days :
		print("   ", end = "")
	elif 0 < day <= number_of_days:
		print("{0:>2}".format(day), end = " ")
	if day == (first_day + 6):
		print("\n", end ="")
	elif day == (first_day + 13):
		print("\n", end ="")
	elif day == (first_day + 20):
		print("\n", end ="")
	elif day == (first_day + 27):
		print("\n", end ="")
	elif day == (first_day + 34):
		print("\n", end ="")
