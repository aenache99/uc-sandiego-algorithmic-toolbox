def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def get_maximum_value(expression: str) -> int:
    n = len(expression)
    digits = []
    operations = []

    # Separate digits and operations
    for i in range(n):
        if i % 2 == 0:
            digits.append(int(expression[i]))
        else:
            operations.append(expression[i])

    m = len(digits)
    max_vals = [[0] * m for _ in range(m)]
    min_vals = [[0] * m for _ in range(m)]

    for i in range(m):
        max_vals[i][i] = digits[i]
        min_vals[i][i] = digits[i]

    # Memoization for intermediate results
    for s in range(1, m):
        for i in range(m - s):
            j = i + s
            min_val = float('inf')
            max_val = float('-inf')
            for k in range(i, j):
                op = operations[k]
                a = evaluate(max_vals[i][k], max_vals[k + 1][j], op)
                b = evaluate(max_vals[i][k], min_vals[k + 1][j], op)
                c = evaluate(min_vals[i][k], max_vals[k + 1][j], op)
                d = evaluate(min_vals[i][k], min_vals[k + 1][j], op)
                min_val = min(min_val, a, b, c, d)
                max_val = max(max_val, a, b, c, d)
            min_vals[i][j] = min_val
            max_vals[i][j] = max_val

    return max_vals[0][m - 1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
