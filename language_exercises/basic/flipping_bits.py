""" You will be given a list of 32 bit unsigned integers. Flip all the bits (1 -> 0) and
 (0 -> 1) and return the result as an unsigned integer."""

import math
def flip_bits(n: int):
    # (1) flip all bits using the bitwise NOT operator
    # (2) convert result to unsigned value, since Python does not have unsigned, add (1 << 32) to convert signed
    #      to unsigned (same as adding 2^32)
    return ~n + (1 << 32)

print(flip_bits(2147483647))
print(flip_bits(1))
print(flip_bits(0))