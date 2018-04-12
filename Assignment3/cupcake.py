# A program that asks a series of questions that evantually leads to a decision about whether to eat the food dropped on the floor or not
# Name: Yifei Yu
# Date: 16th March 2018
# Course: CSC1015F



print('Welcome to the 30 Second Rule Expert')
print('------------------------------------')
print('Answer the following questions by selecting from among the options.')
r = input('Did anyone see you? (yes/no)\n')
if r == 'no':
	r = input('Was it sticky? (yes/no)\n')
	if r == 'no':
		r = input('Is it an Emausaurus? (yes/no)\n')
		if r == 'no':
			r = input('Did the cat lick it? (yes/no)\n')
			if r == 'no':
				decision = 'Eat it.'
			else:
				r = input('Is your cat healthy? (yes/no)\n')
				if r == 'no':
					decision = 'Your call.'
				else:
					decision = 'Eat it.'
		else:
			r = input('Are you a Megalosaurus? (yes/no)\n')
			if r == 'no':													
				decision = "Don't eat it."   
			else:
				decision = 'Eat it.'
	else:
		r = input('Is it a raw steak? (yes/no)\n')
		if r == 'no':
			r = input('Did the cat lick it? (yes/no)\n')				
			if r == 'no':
				decision = 'Eat it.'
			else:
				r = input('Is your cat healthy? (yes/no)\n')
				if r == 'no':		
					decision = 'Your call.'
				else:	
					decision = 'Eat it.'		
		else:					
			r = input('Are you a puma? (yes/no)\n')
			if r == 'no':
				decision = "Don't eat it."					
			else:
				decision = 'Eat it.'
else:						
	r = input('Was it a boss/lover/parent? (yes/no)\n')
	if r=='no':
		decision = 'Eat it.'
	else:
		r = input('Was it expensive? (yes/no)\n')
		if r == 'no':
			r = input('Is it chocolate? (yes/no)\n')
			if r == 'no':
				decision= "Don't eat it."				
			else:
				decision = 'Eat it.'
		else:
			r = input('Can you cut off the part that touched the floor? (yes/no)\n')						
			if r == 'no':
				decision = 'Your call.'
			else:
				decision = 'Eat it.'
print('Decision:', decision)
