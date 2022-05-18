
def multiplicate(A):

    if len(A) < 2:
        return [None]

    mult_a = 1
    for a in A:
        mult_a *= a

    return [int(mult_a/a) for a in A]


if __name__ == '__main__':
    import random
    A_test = [random.randint(1, 101) for _ in range(4)]

    print('Test A :', A_test)
    print('Answer :', multiplicate(A_test))
