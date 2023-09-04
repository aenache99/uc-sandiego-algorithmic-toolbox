def euclidGCD(a, b):
    if b == 0:
        return a
    a_prime = a % b
    return euclidGCD(b, a_prime)


def lcm(a, b):
    return int((a * b) / euclidGCD(a, b))


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))
