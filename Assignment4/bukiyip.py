# This module is to conduct calculation based in the Bukiyip language
# Student Name: Yifei Yu
# Course Code: CSC1015F

def bukiyip_to_decimal(a):
	"""Return the decimal value of a bukiyip number"""
	first_digit = a % 10
	second_digit = (a // 10) % 10
	third_digit = (a // 10) // 10	
	decimal = third_digit * 9 + second_digit * 3 + first_digit
	return decimal

def decimal_to_bukiyip(a):
	"""Return the bukiyip equivalent of given decimal value"""
	first_digit = a % 3
	second_digit = (a % 9) // 3
	third_digit = a // 9
	bukiyip = third_digit * 100 + second_digit * 10 + first_digit
	return bukiyip

def bukiyip_add(a, b):
	"""Return the bukiyip value of addition of two given bukiyip numbers"""
	import bukiyip
	decimal_addition = bukiyip_to_decimal(a) + bukiyip_to_decimal(b)
	bukiyip_addition = decimal_to_bukiyip(decimal_addition)
	return bukiyip_addition

def bukiyip_multiply(a, b):
	"""Return the multiplication result of two bukiyip number"""
	import bukiyip
	decimal_multiplication = bukiyip_to_decimal(a) * bukiyip_to_decimal(b)
	bukiyip_multiplication = decimal_to_bukiyip(decimal_multiplication)
	return bukiyip_multiplication
