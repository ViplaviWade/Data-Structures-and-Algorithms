# Move zeros and append to the last
def moveZeros(nums):
    for i in range(len(nums)):
        if 0 in nums:
            nums.remove(0)
            nums.append(0)
    print(nums)
moveZeros(nums = [0,1,0,3,12])