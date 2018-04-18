# This module contains 5 different functions that together forms the answer to Assignment 4 Question 1
# Student Name: Yifei Yu
# Course Code: CSC1015F

# Function1: Given a year (a 4 digit number), returns true if it is a leap year, and false otherwise.
def is_leap_year(year):
	"""Return True or False depending on if it's a leap year"""
	if year % 400 ==0:
		return True
	if year % 100 == 0:
		return False
	if year % 4 == 0:
		return True
	else:
		return False

def month_name(number):
	""""Return the name of the month"""
	if number == 1:
		return "January"
	elif number == 2:
		return "February"
	elif number == 3:
		return "March"
	elif number == 4:
		return "April"
	elif number == 5:
		return "May"
	elif number == 6:
		return "June"
	elif number == 7:
		return "July"
	elif number == 8:
		return "August"
	elif number == 9:
		return "September"
	elif number == 10:
		return "October"
	elif number == 11:
		return "November"
	elif number == 12:
		return "December"

def days_in_month(month_number, year):
	"""Return the number of days in a given number of the month"""
	import calutils
	if is_leap_year(year) == False:
		if month_number == 1:
			return 31
		if month_number == 2:
			return 28
		if month_number == 3:
			return 31
		if month_number == 4:
			return 30
		if month_number == 5:
			return 31
		if month_number == 6:
			return 30
		if month_number == 7:
			return 31
		if month_number == 8:
			return 31
		if month_number == 9:
			return 30
		if month_number == 10:
			return 31
		if month_number == 11:
			return 30
		if month_number == 12:
			return 31
	else:
		if month_number == 1:
                        return 31
		if month_number == 2:
                        return 29
		if month_number == 3:
                        return 31
		if month_number == 4:
                        return 30
		if month_number == 5:
                        return 31
		if month_number == 6:
                        return 30
		if month_number == 7:
                        return 31
		if month_number == 8:
                        return 31
		if month_number == 9:
                        return 30
		if month_number == 10:
                        return 31
		if month_number == 11:
                        return 30
		if month_number == 12:
                        return 31
def first_day_of_year(year):
	day = 5 * ((year - 1) % 4)	
	day = 1 + day + 4 * ((year - 1) % 100)
	day = day + 6 * ((year - 1) % 400)
	day = day % 7
	return day
def first_day_of_month(month_number, year):
	from datetime import datetime
	datetime_code = ["6","0","1","2","3","4","5"]
	assignment_code = ["0","1","2","3","4","5","6"]
	datetime_convert_dict = dict(zip(datetime_code,assignment_code))
	day = datetime(year,month_number,1).weekday()
	final_output = int(datetime_convert_dict[str(day)])
	return final_output

