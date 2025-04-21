def heapify_at_index(arr, i, heap_size):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    if right < heap_size and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_at_index(arr, largest, heap_size)

def heap_sort(arr):
    n = len(arr)
    for i in range(n//2-1, -1, -1):
        heapify_at_index(arr, i, n)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify_at_index(arr, 0, i)
    return arr

arr = list(map(int, input("Enter array elements: ").split()))
res = heap_sort(arr)
print("Sorted array: ", res)