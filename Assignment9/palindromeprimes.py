import sys
sys.setrecursionlimit (200000)

def main():
	start_point = input("Enter the starting point N:\n")
	end_point = input("Enter the ending point M:\n")
	print("The palindromic primes are:")
	find_palindrome(int(start_point), int(end_point))








def find_palindrome(start_point, end_point):
	if end_point >= start_point:
		if is_palindrome(str(start_point)):
			if is_prime(start_point):
				print(start_point)
				return find_palindrome(start_point+1, end_point)
			else:
				return find_palindrome(start_point+1, end_point)
		else:
			return find_palindrome(start_point+1, end_point)

def is_palindrome(n):
	if n != "":
		if n[0] == n[-1]:
			return is_palindrome((n)[1:-1])
		else:
			return False
	else:
		return True		








def is_prime(n, x=2):
	if n == 0 or n ==1:
		return False
	elif n == x:
		return True
	else:
		if n % x != 0:
			return is_prime(n, x+1)
		else:
			return False



if __name__ == "__main__":
	main()
