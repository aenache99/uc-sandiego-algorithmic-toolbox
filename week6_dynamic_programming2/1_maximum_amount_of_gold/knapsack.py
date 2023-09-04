from typing import List


def optimal_weight(capacity: int, weights: List[int]) -> int:
    n = len(weights)
    value = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        elem = weights[i - 1]
        for w in range(1, capacity + 1):
            value[i][w] = value[i - 1][w]

            if elem <= w:
                val = value[i - 1][w - elem] + elem
                if value[i][w] < val:
                    value[i][w] = val

    return value[n][capacity]


if __name__ == '__main__':
    W, n = map(int, input().split())
    w = list(map(int, input().split()))
    print(optimal_weight(W, w))
