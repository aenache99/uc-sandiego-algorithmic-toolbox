# Uses python3
import random


def quick_sort_2p(arr, low, high):
    """
    Quick sort algorithm (2 partitions).
    Works inplace.

    Algorithm:
    1. Randomly select pivot element.
    2. Split array into two parts:
    - elements less than pivot element
    - elements greater or equal than pivot element
    3. Recursively sort elements less than pivot element.
    4. Sort elements greater or equal than pivot element
    with tail recursion elimination.
    """
    while low < high:
        pivot_i = random.randint(low, high)
        pivot = arr[pivot_i]
        arr[pivot_i], arr[low] = arr[low], arr[pivot_i]

        split = low  # last index of elements less than pivot element

        for i in range(low + 1, high + 1):
            if arr[i] < pivot:
                arr[i], arr[split + 1] = arr[split + 1], arr[i]
                split += 1
        arr[low], arr[split] = arr[split], arr[low]
        split -= 1

        quick_sort_2p(arr, low, split)
        low = split + 1


def quick_sort_3p(arr, low, high):
    """
    Quick sort algorithm (3 partitions).
    Works inplace.
    Improved version to deal with lots of identical elements.

    Algorithm:
    1. Randomly select pivot element.
    2. Split array into three! parts:
    - elements less than pivot element
    - elements equal to pivot element!
    - elements greater than pivot element
    3. Recursively sort elements less than pivot element.
    4. Sort elements greater than pivot element with tail
    recursion elimination.
    """
    while low < high:
        pivot_i = random.randint(low, high)
        pivot = arr[pivot_i]
        arr[pivot_i], arr[low] = arr[low], arr[pivot_i]

        split1 = low  # last index of elements less than pivot element
        split2 = low  # last index of elements equal to pivot element

        for i in range(low + 1, high + 1):
            if arr[i] < pivot:
                if split1 == split2:  # no middle part of pivot elements
                    arr[i], arr[split1 + 1] = arr[split1 + 1], arr[i]
                else:
                    arr[split1 + 1] = arr[i]
                    arr[i] = arr[split2 + 1]
                    arr[split2 + 1] = pivot
                split1 += 1
                split2 += 1
            elif arr[i] == pivot:
                arr[i] = arr[split2 + 1]
                arr[split2 + 1] = pivot
                split2 += 1
        arr[low], arr[split1] = arr[split1], arr[low]
        split1 -= 1

        quick_sort_3p(arr, low, split1)
        low = split2 + 1


if __name__ == '__main__':

    n = int(input())
    arr = list(map(int, input().split()))
    quick_sort_3p(arr, 0, n - 1)
    for x in arr:
        print(x, end=' ')
