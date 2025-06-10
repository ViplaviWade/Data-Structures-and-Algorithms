# Bubble sort. Sorting a pair(2 elements) swapping them
def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = list(map(int, input("Enter numbers: ").split()))
res = bubble_sort(arr)
print("Sorted array is: ",res)