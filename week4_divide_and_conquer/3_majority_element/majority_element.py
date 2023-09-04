def majority_element_boyer_moore(arr):
    candidate = None
    count = 0

    for num in arr:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1

    if arr.count(candidate) > len(arr) // 2:
        return 1
    else:
        return 0


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    result = majority_element_boyer_moore(arr)
    print(result)
