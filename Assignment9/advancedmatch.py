# A function that can be used to determine if a given pattern matches a given word
def match(pattern, word):
	if pattern != "" and word != "":
		if pattern[0] == word[0]:
			return match(pattern[1:], word[1:])
		elif pattern[0] == "?":
			return match(pattern[1:], word[1:])
		elif pattern[0] == "*":
			if len(pattern) != 1 and len(word) != 1:
				if pattern[1] == word[1]:
					if len(pattern) != 2 and len(word) != 2:
						return match(pattern[2:], word[2:])
					elif len(pattern) == 2 and len(word) == 2:
						return match(pattern[1:], word[1:])
				elif pattern[1] == word[2]:
					return match(pattern[1:], word[2:])
				else:
					if pattern[-1] == "*":
						if pattern[-2] == word[-2]:
							return match(pattern[:-2], word[-2])
					if pattern[-1] == word[-1]:
						return match(pattern[:-1], word[:-1])
			else:
				return match(pattern[:-1], word[:-1])
	elif pattern == "" or word == "":
		return True
	else:
		return False







