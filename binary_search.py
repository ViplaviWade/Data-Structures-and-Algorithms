# Find a specific number using Binary search
def apply_binary_search(arr, start, end, num):
        mid = (start+end)//2
        if num == arr[mid]:
            return f"Number found at position {mid}"
        if num > mid:
            apply_binary_search(arr, mid, end, num)
        else:
            apply_binary_search(arr, start, mid-1, num)

def binary_search(arr, num):
    n = len(arr)
    mid = n//2
    if num == arr[mid]:
            return f"Number found at position {arr[mid]}"
    if num > mid:
        apply_binary_search(arr, mid, n, num)
    else:
        apply_binary_search(arr, 0, mid-1, num)



arr = list(map(int, input("Enter sorted list of array: ").split()))
num = int(input("Enter the number to search: "))
res = binary_search(arr, num)
print(res)