# Remove element

def removeElement(nums, val):
    while val in nums:
        nums.remove(val)
    return nums

res = removeElement(nums = [3, 2, 2, 3], val = 3)
print(res)