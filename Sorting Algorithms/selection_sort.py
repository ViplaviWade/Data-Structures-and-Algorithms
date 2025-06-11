# Selection sort. Finds the smallest element and swaps it into place(at start of the array)

def selection_sort(arr):
    n = len(arr)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr


arr = list(map(int, input("Enter array numbers: ").split()))
sorted_list = selection_sort(arr)
print("Sorted List: ", sorted_list)