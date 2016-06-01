# Problem 97:
#
# Determine the last 10 digits of 28433 * 2^7830457 + 1.
# Our strategy will be to first compute the mod 10^10 remainder of the power
# of two part of the number by successive squaring and reduction.  Then the
# final part of the computation is easy.

from math import log, floor

exponent = 7830457
coefficient = 28433


def mod_reduction_of_power_of_2():
    number_of_squarings = int(floor(log(exponent, 2)))
    remaining_mult_of_2 = exponent - 2**number_of_squarings
    # Compute 2 ^ (2 ^ number_of_squarings)
    result = 2
    for _ in xrange(number_of_squarings):
        result = (result * result) % 10**10
    # Multiply by 2 until the 
    for _ in xrange(remaining_mult_of_2):
        result = (result * 2) % 10**10
    print ex
    return result

if __name__ == '__main__':
    result = mod_reduction_of_power_of_2()
    result = (coefficient * result + 1) % 10**10
    print(result)

