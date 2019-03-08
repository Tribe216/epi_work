from test_framework import generic_test


def plus_one(A):
    # TODO - you fill in here.
    a = A
    for x in range(len(a)-1, -1, -1):
        a[x] = (a[x] + 1) % 10
        if a[x] != 0:
            break
        if x == 0:
            a.insert(0, 1)

    return a
        

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
