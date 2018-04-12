# CSC1015F Assignment1 spam.py
# Student Name: Yifei Yu
# Student ID: YXXYIF001

# Ask the user for input of names, amount of money and county
first_name = input("Enter first name:\n")
last_name = input("Enter last name:\n")
money = eval(input("Enter sum of money in USD:\n"))
country = input("Enter country name:\n")

# print out the spam message with variables from the input
print("\nDearest", first_name)
print("It is with a heavy heart that I inform you of the death of my father,")
print("General Fayk", last_name, end="")
print(", your long lost relative from Mapsfostol.")
print("My father left the sum of", money, end="")
print("USD for us, your distant cousins.")
print("Unfortunately, we cannot access the money as it is in a bank in", country, end=".")
print("\nI desperately need your assistance to access this money.")
print("I will even pay you generously, 30% of the amount -", 0.3*money, end="")
print("USD,")
print("for your help.  Please get in touch with me at this email address asap.")
print("Yours sincerely")
print("Frank", last_name)
