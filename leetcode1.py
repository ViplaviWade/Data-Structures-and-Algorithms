def twoSum(nums = [2,7,11,15], target = 9):
    n = len(nums)
    arr = []
    for i in range(n-1):
        for j in range(i+1, n):
            sum = nums[i] + nums[j]
            if sum == target:
                arr.append(i)
                arr.append(j)
    print(arr)

twoSum()