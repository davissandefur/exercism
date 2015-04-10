def sum_of_multiples(number, factors=[3, 5]):
    """ This function returns the sum of all multiples of 3 and 5 up to but not including (number). Factors is initialized so it uses the list [3,5], per instructions"""
    if factors[0] == 0:
        factors = factors[1:]
    return sum(value for value in range(number) if any(value % factor == 0 for factor in factors))
