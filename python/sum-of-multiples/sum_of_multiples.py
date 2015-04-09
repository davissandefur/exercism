def sum_of_multiples(factor=6, multiples=[3, 5]):
    """ This function returns the sum of all multiples of 3 and 5 up to but not including (factor). Factor is
    initalized as 6 so that if not factor is given, it uses the list [3,5], per instructions"""
    if multiples[0] == 0:
        multiples = multiples[1:]
    return sum(value for value in range(factor) if any(value % multiple == 0 for multiple in multiples))