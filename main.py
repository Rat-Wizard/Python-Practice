import time
from bubbleSort import bubbleSort
from quickSort import quickSort
from helper import printArr
from helper import generateArray

def sort(sortFunction, *args):
    startTime = time.time()
    sortFunction(*args)  
    endTime = time.time()
    executionTime = endTime - startTime
    printArr(args[0])  
    return executionTime

arr = generateArray(1, 100, 100)

bubbleTime = sort(bubbleSort, arr)
print(f"Bubble Sort Execution Time: {bubbleTime:.6f} seconds")

quickSortTime = sort(quickSort, arr, 0, len(arr)-1)
print(f"Quick Sort Execution Time: {quickSortTime:.6f} seconds")
