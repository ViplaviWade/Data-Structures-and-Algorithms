# Remove element

def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
        return k

res = removeElement(nums = [3, 2, 2, 3], val = 3)
print(res)