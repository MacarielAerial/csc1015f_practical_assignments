# techsupport.py

def welcome():
        print("Welcome to the automated technical support system.")
        print("Please describe your problem:")

def get_input():
        return input().lower()

def response_dict():
	response_keywords = ['crashed', 'blue', 'hacked', 'bluetooth', 'windows', 'apple', 'spam', 'connection']
	response = ['Are the drivers up to date?', 'Ah, the blue screen of death. And then what happened?', 'You should consider installing anti-virus software.', 'Have you tried mouthwash?', 'Ah, I think I see your problem. What version?', 'You do mean the computer kind?', 'You should see if your mail client can filter messages.', 'Contact Telkom.']
	response_dict = dict(zip(response_keywords, response))
	return response_dict

def main():
	welcome()
	query = get_input()
	query_splited = str(query).split()
	while query != 'quit':
		if any(word in response_dict().keys() for word in query_splited):
			for word in query_splited:
				if word in response_dict().keys():
					print(response_dict()[word])
					break
			query = get_input()
			query_splited = str(query).split()
		else:
			print('Curious, tell me more.')
			query = get_input()
			query_splited = str(query).split()

if __name__ == "__main__":
	main()
