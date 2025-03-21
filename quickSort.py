from helper import swap
from helper import printArr

def partition(arr, min, max):
    pivot = arr[max]

    j = min - 1
    for i in range (min, max):
        if arr[i] < pivot:
            j += 1
            swap(arr, j, i)

    swap(arr, j + 1, max)
    return j + 1


def quickSort(arr, min, max):
   
    if min < max:
        n = partition(arr, min, max)

        quickSort(arr, min, n-1)
        quickSort(arr, n+1, max)

