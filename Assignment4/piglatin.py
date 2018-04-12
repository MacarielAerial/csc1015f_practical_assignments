# This is the module for piglatin

def to_pig_latin(sentence):
	sentence1 = sentence.split()
	consonant = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","x","z"]
	final_output = ""
	for word in sentence1:
		word1 = str(word)
		if word1[0:1] in "aeiou":
			word1 = word1 + "way"	
		else:
			word1 = word1 + "a"
			for char in word1:
				if char in consonant:
					word1 = word1.replace(char,"")
					word1 = word1 + char
				else:
					break
			word1 = word1 + "ay"
		final_output = final_output + " " + word1
	return final_output[1:]
		
	
if __name__ == "__main__":
	sentence = input("What's the English sentence that you wish to convert to pig-latin?:\n")
	print(to_pig_latin(sentence))
