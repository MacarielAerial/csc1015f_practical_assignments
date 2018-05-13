# the program obtain an acronym for a given sentence

# List of ignored words
black_list_item = input("Enter words to be ignored separated by commas:\n")
black_list_upper = black_list_item.split(', ')
black_list = []
for item in black_list_upper:
	item = item.lower()
	black_list.append(item)
# List of strings to make acronym of
title_item = input("Enter a title to generate its acronym:\n")
title = title_item.split(" ")
# Operate on each individual string
acronym = ''
for word in title:
	if not word.lower() in black_list:
		acronym += word[0].upper()
print("The acronym is:", acronym)	
