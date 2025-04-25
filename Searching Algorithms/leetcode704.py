# Binary Search: search a number in a sorted array

def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

res = search(nums=[-1, 0, 3, 5, 9, 12], target=9)
print(res)