# Check for duplicates in array

def containsDuplicate(nums):
    return len(nums) != len(set(nums))

containsDuplicate(nums=[1, 2, 3, 1])