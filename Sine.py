import math

# define x
x = math.pi / 2

# calculate
sine = 0

num = x
den = 1
den_base = 1
sign = 1

term = sign * num / den

# countinue the taylor series until
# our term is smaller than epsilon
epsilon = 0.000000000000000000000001

while abs(term) > epsilon:
	sine += term

	num *= x * x
	den_base += 2
	den *= den_base * (den_base - 1)
	sign *= -1

	term = sign * num / den
# done!
print(sine)
