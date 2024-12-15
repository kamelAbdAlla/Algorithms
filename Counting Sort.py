import sys
from typing import List


def read_input() -> List[int]:
   
    try:
        arr = list(map(int, input("Enter unsorted array: ").strip().split()))
    except ValueError:
        sys.exit("Only integer values expected for sorting.")

    return arr


def counting_sort(unsorted: List[int]) -> List[int]:
   
    size = len(unsorted)
    minm, maxm = min(unsorted), max(unsorted)  # Step 1
    counter = [0] * (maxm - minm + 1)  # Step 2

    for element in unsorted:  # Step 3
        counter[element - minm] += 1  # treating minm element as zero index

    for idx in range(1, maxm - minm + 1):  # Step 4
        counter[idx] += counter[idx - 1]

    # Step 5
    result = [0] * size
    n = size - 1
    while n >= 0:
        # processing unsorted elements in reverse order
        # sorted list is built without any particular order
        current = unsorted[n]
        result[counter[current - minm] - 1] = current
        counter[current - minm] -= 1  # update count after processing an element
        n -= 1
    return result


if __name__ == "__main__":
    unsorted = read_input()
    result = counting_sort(unsorted)
    print(f"Sorted elements: {result}\n")