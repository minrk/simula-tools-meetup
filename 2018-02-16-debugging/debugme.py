def div(x, y):
    return x / y


def sub(x, n):
    return x - n


def solve(x, y):
    y2 = sub(y, 1)
    return div(x, y2)


def main():
    solve(2, 1)


if __name__ == '__main__':
    main()
