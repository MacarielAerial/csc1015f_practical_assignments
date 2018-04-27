# vectormath.py
import math
def main():
	# input
	vector_a_input = input("Enter vector A:\n")
	vector_a = vector_a_input.split()
	vector_b_input = input("Enter vector B:\n")
	vector_b = vector_b_input.split()
	a_plus_b = []
	a_times_b = 0
	a_norm_square = 0
	b_norm_square = 0
	# logical calculation
	for dimension in range(3):
		a_plus_b.append(int(vector_a[dimension]) + int(vector_b[dimension]))
		a_times_b = a_times_b + (int(vector_a[dimension])*int(vector_b[dimension]))
		a_norm_square = a_norm_square + int(vector_a[dimension])**2
		b_norm_square = b_norm_square + int(vector_b[dimension])**2
	# output
	print("A+B = ", a_plus_b, sep="")
	print("A.B = ", a_times_b, sep="")
	print("|A| = ", "{0:.2f}".format(math.sqrt(a_norm_square)), sep="")
	print("|B| = ", "{0:.2f}".format(math.sqrt(b_norm_square)), sep="")


if __name__ == "__main__":
	main()
