# swap, partitioning, quickSort(recursion)
# low index, high index, store index, pivot value, pivot index
from random import randint

def swap(array, i, j):
    _ = array[i]
    array[i] = array[j]
    array[j] = _


def partitioning(array, low, high):
    pivotIndex = randint(low, high)
    pivotValue = array[pivotIndex]

    swap(array, pivotIndex, high)

    storeIndex = low

    for i in range(low, high):
        if array[i] < pivotValue:
            swap(array, i, storeIndex)
            storeIndex = storeIndex +1
    swap(array, storeIndex, high)

    return storeIndex


def quicksort(array, low, high):
    if low < high:
        partition = partitioning(array, low, high)
        quicksort(array, low, partition-1)
        quicksort(array, partition+1, high)


A = [randint(0, 100) for _ in range(15)]
print(A)
quicksort(A, 0, len(A)-1)
print(A)

