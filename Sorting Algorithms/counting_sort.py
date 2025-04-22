def counting_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    count = [0] * (max_val+1)
    sorted_arr = []
    for i in arr:
        count[i] += 1
    for i in range(len(count)):
        sorted_arr.extend([i]*count[i])

    return sorted_arr

arr = list(map(int, input("Enter array elements: ").split()))
res = counting_sort(arr)
print("Sorted array: ", res)