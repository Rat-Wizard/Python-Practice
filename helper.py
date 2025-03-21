import random

def generateArray(start, end, n):
    arr = [random.randint(start, end) for _ in range(n)]
    return arr

def swap(arr, first, second):
    arr[first], arr[second] = arr[second], arr[first]

def printArr(arr):
    for i in arr:
        print(i, end=", " if i != arr[-1] else "")
    print() 