# The module contains a function that can be used to determine if a given pattern matches a given word
def match(pattern, word):
	if pattern != "" and word != "":
		if pattern[0] == word[0]:
			return match(pattern[1:], word[1:])
		elif pattern[0] == "?":
			return match(pattern[1:], word[1:])
		else:
			return False
	elif pattern == "" and word == "":
		return True
	else:
		return False	
