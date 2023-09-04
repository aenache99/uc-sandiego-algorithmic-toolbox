def max_pairwise_product(numbers):
    n = len(numbers)

    # Find the two largest numbers in the list
    max1 = max(numbers)
    numbers.remove(max1)
    max2 = max(numbers)

    max_product = max1 * max2

    return max_product


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))