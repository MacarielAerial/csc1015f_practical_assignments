# This program finds all palindromic primes between two integers supplied as input
# Student Name: Yifei Yu
# Date: 24th March 2018
# Course Code: CSC1015F

# Request input
start_point = eval(input("Enter the start point N:\n"))
end_point = eval(input("Enter the end point M:\n"))

# Prepare for output
print("The palindromic primes are:\n", end ="")

# Reverse number that is inputed
for all_integer in range(start_point +1, end_point):
	if all_integer % 10 != 0:
		reverse = 0
		original_integer = all_integer
		while all_integer >0:
			remainder = all_integer % 10
			reverse = (reverse * 10) + remainder
			all_integer = all_integer // 10
		if reverse == original_integer:
			isprime = True
			for prime_check in range(2,reverse):
				if reverse % prime_check == 0:
					isprime = False
			if isprime == True:
				print(reverse, end="\n")

