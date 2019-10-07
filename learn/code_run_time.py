from time_sum import TimeSum


def add(a, b):
    return f'a:{a}, b:{b},a+b={a + b}'


if __name__ == '__main__':
    with TimeSum():
        for i in range(1000000):
            add(i, i)
