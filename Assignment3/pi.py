# This program calculates the value of PI and then computes and displays the area of a circle with radius entered by the user.
# Student Name: Yifei Yu
# Date: 16th March 2018
# Course: CSC1015F

import numpy as np

# boolean telling while loop if the last term was close enough to the desired number
not_precise_enough = True
number_of_decimals = 10

# calculate two first terms manually
pi = 2.0
ledd = np.sqrt(2)

pi = pi * 2.0 / ledd

#while-loop run until requirment is meet
while(not_precise_enough):
    ledd = 2.0 / np.sqrt(2.0 + np.power(ledd/2.0,-1))
    pi = pi * ledd

    #change boolean if within 'x' decimals of 1
    if(np.round(ledd, decimals = number_of_decimals) == 1.0):
        not_precise_enough = False

print("Approximation of pi:", round(pi,3))
input_radius = float(input("Enter the radius:\n"))
print("Area:", pi * np.power(input_radius,2))
	
