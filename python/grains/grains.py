def on_square(number):
	if number == 1:
		return 1
	else:
		return 2 * on_square(number - 1)

def total_after(number):
	return sum([on_square(x) for x in range(1,number+1)])

