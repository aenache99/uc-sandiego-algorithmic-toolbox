def can_partition3(weights):
    total_weight = sum(weights)

    if total_weight % 3 != 0:
        return False

    target_sum = total_weight // 3
    n = len(weights)

    # Create a 2D array to represent whether it's possible to form partitions
    dp = [[False] * (target_sum + 1) for _ in range(n + 1)]

    # Initialization: It's always possible to form zero partitions with a sum of zero
    for i in range(n + 1):
        dp[i][0] = True

    # Dynamic programming
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= weights[i - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j - weights[i - 1]]

    # Check if it's possible to form three partitions with a sum of target_sum
    return dp[n][target_sum]


if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    if can_partition3(A):
        print(1)
    else:
        print(0)
