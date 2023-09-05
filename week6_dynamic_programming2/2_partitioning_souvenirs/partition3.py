def can_partition3(A):
    total_sum = sum(A)

    # Check if the total sum is divisible by 3
    if total_sum % 3 != 0:
        return 0

    target_sum = total_sum // 3
    n = len(A)

    def backtrack(index, subset_sum, subsets):
        if index == n:
            # Check if all subsets have reached the target sum
            return all(subset_sum[i] == target_sum for i in range(3))

        for i in range(3):
            if subset_sum[i] + A[index] <= target_sum:
                subset_sum[i] += A[index]
                subsets[index] = i

                if backtrack(index + 1, subset_sum, subsets):
                    return 1

                subset_sum[i] -= A[index]
                subsets[index] = -1

        return 0

    subsets = [-1] * n  # Initialize subsets array
    return backtrack(0, [0, 0, 0], subsets)


if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    print(can_partition3(A))
