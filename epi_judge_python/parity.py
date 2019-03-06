from test_framework import generic_test


def parity(x):
    # TODO - you fill in here.
    par = 0

    while x > 0:
        par ^= x & 1
        x >>= 1

    return par


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
