# This is the module for piglatin

def to_pig_latin(sentence):
	sentence1 = sentence.split()
	consonant = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","x","z"]
	vowel = ["a","e","i","o","u"]
	final_product = ""
	for word in sentence1:
		word1 = ""
		for index in range(len(word)):
			if word[index] in vowel:
				if index == 0:
					word1 = word + "way"
					break
			if word[index] in consonant:
				word1 = word1 + word[index]
				if index == len(word) - 1:
					if word[index] in consonant:
						word1 = "a" + word1 + "ay"
						break
			else:
				word1 = word[index:] + "a" +  word1 + "ay"
				break
		final_product = final_product + " " + word1
	return final_product[1:]

def to_english(sentence):
	sentence1 = sentence.split()
	consonant = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","x","z"]
	vowel = ["a","e","i","o","u"]
	final_product = ""
	for word in sentence1:
		word1 = ""
		if word[len(word)-3:len(word)] == "way":
			word1 = word[:len(word)-3]
		else:
			for index in range(-3,-len(word)-1,-1):
				if word[index] in consonant:
					word1 = word[index] + word1
				else:
					word1 = word1 + word[-len(word):index]
					break
		final_product = final_product + " " + word1
	return final_product[1:]
	
if __name__ == "__main__":
	choice = input("Enter (E) if you want to convert English to Pig Latin or Enter (P) if you want to convert Pig Latin to English:\n")
	if choice == "E":
		sentence = input("What's the English sentence that you wish to convert to pig-latin?:\n")
		print(to_pig_latin(sentence))
	if choice == "P":
		sentence = input("What's the Pig Latin sentence that you wish to convert to English?:\n")
		print(to_english(sentence))
