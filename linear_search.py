# Linear Search algorithm to find the lowest value in the array

def linear_search(arr):
    minVal = arr[0]
    for i in range(len(arr)):
        if arr[i] < minVal:
            minVal = arr[i]
    return minVal



n = int(input("Enter length of array: "))
arr = list(map(int, input("Enter numbers: ").split()))
minVal = linear_search(arr)
print("Lowest value in the array is: ", minVal)