from test_framework import generic_test
from functools import reduce

words = {}
word_size = 16
bit_mask = pow(2, word_size) -1

def parity(x):
    # TODO - you fill in here.
    par = 0

    while x > 0:
        x = x & (x - 1)
        par ^= 1

    return par

#preload all subword parities
for i in range(bit_mask + 1):
    words[i] = parity(i)

def cached_parity(x):
    # TODO - you fill in here.
    parity_tracker = 0
    for i in range(4):
        sub_word = (x >> (word_size * i)) & bit_mask
        parity_tracker ^= words[sub_word]
    return parity_tracker


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', cached_parity))
