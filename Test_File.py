import math
for row in range(10,-11,-1):
	for col in range(0,41):
		x = col/40 * 2 * math.pi
		y = row/10
		
		sine = 0
		num = x
		den = 1
		den_base = 1
		sign = 1
		
		term = sign * num/den

		epsilon = 0.0000000000000001
		
		while abs(term) > epsilon:
			sine = sine + term
			num *= x * x
			den_base += 2
			den *= den_base * (den_base-1)
			sign *= -1

			term = sign * num/den

		if abs(y - sine) < 1/40:
			print("X", end="")
		elif row == 0:
			print("-", end="")
		elif col == 0:
			print("|", end="")
		else:
			print(" ", end="")
	print()
