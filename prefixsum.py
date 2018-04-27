# This script contains a function that outputs a prefix sum array with an input array

def prefix_sum(input_array):
	output_array = []
	for index in range(len(input_array)):
		output_array.append(input_array[index])

	for index in range(len(input_array)):
		if index == 0:
			output_array[index] = input_array[index]
		else:
			output_array[index] = input_array[index] + output_array[index - 1]
	return output_array


if __name__ == "__main__":
	i = 1
	input_array = []
	while True:
		input_array_item = input("Enter the" + " " + str(i) + "th" + " " + "number that you wish to include in the list: ")
		if input_array_item == "":
			break
		i += 1
		input_array += [int(input_array_item)]
	print(prefix_sum(input_array))
