def slices(sequence, length):
    """ This function takes a sequence of numbers and returns all possible slices of a certain length as a list.
     If the length is greater than the length of the sequence, a value error is raised """

    if length > len(sequence) or length == 0:
        raise ValueError('Length is greater than sequence')

    slices = []

    index_counter = 0

    while index_counter + length <= len(sequence):
        slices.append([int(i) for i in sequence[index_counter:index_counter+length]])
        index_counter += 1

    return slices

def largest_product(sequence, length):
	if length == 0:
		return 1;
	list = slices(sequence, length)
	highest_product = 0
	for slice in list:
		product = 1
		for i in slice:
			product *= i
		if product > highest_product:
			highest_product = product

	return highest_product
