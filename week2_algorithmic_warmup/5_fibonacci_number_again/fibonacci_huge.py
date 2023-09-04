def get_pisano_period_length(m):
    a, b = 0, 1
    for i in range(0, m * m):
        a, b = b, (a + b) % m
        if a == 0 and b == 1:
            return i + 1


def fibonacci_huge_naive(n, m):

    remainder = n % get_pisano_period_length(m)
    previous = 0
    current = 1

    res = remainder

    for _ in range(1, remainder):
        res = (previous + current) % m
        previous = current
        current = res

    return res % m


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))
