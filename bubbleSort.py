from helper import swap

def bubbleSort(arr):
    n = len(arr)

    for i in range (n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)
