# The program identifies palindrome from a string input from the user
def palindrome_identify(a_string):
	if a_string != "":
		if a_string[0] == a_string[-1]:
			return palindrome_identify(a_string[1:-1])
		else:
			return False
	else:	
		return True



def main():
	a_string = input("Enter a string:\n")
	if a_string != "":
		a_string_lower = a_string.lower()
		if palindrome_identify(a_string_lower):
			print("Palindrome!")
		else:
			print("Not a palindrome!")










if __name__ == "__main__":
	main()
