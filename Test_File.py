# A field for experimentation
# Yifei Yu

# Request input
height = eval(input("Enter the desirable height: "))


# Execute loop
for row_number in range(height):
	for number_of_space in range(row_number,0,-1):
		print(" ", end="")
	for number_of_star in range(row_number):
		print("*", end="")
	print()

