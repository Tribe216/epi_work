from test_framework import generic_test
from math import log

def reverse_bits(x):
    # TODO - you fill in here.
    result = 0
    for i in range(64):
        if (x >> i & 1):
            result += pow(2, 63 - i)
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_bits.py", "reverse_bits.tsv",
                                       reverse_bits))
