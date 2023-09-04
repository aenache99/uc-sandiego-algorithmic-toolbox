def binary_search(keys, query):
    left, right = 0, len(keys) - 1
    result = -1  # Initialize result to -1

    while left <= right:
        mid = left + (right - left) // 2  # Calculate the middle index

        if keys[mid] == query:
            result = mid  # Update the result and continue searching to the left
            right = mid - 1
        elif keys[mid] < query:
            left = mid + 1
        else:
            right = mid - 1

    return result

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
