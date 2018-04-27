# support.py

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
	while query != 'quit':
		if query in response_dict():
			print(response_dict()[query])
			query = get_input()
		else:
			print('Curious, tell me more.')
			query = get_input()

if __name__ == "__main__":
	main()
