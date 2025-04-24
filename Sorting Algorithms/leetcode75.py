# Sort colors [2, 0, 2, 1, 1, 0]
# Used counting sort but modifying nums in-place
# Why counting sort? Because some numbers repeat, and numbers in not very big < 100
# Basically count the frequencies and print them


def sort_colors(nums):
    if not nums:
        return nums
    max_val = max(nums)
    count = [0]*(max_val+1)
    k = 0

    for i in nums:
        count[i] += 1
    print(count)
    for i in range(len(count)):
        for j in range(count[i]):
            nums[k] = i
            k += 1
    return nums

nums = [2, 0, 2, 1, 1, 0]
res = sort_colors(nums)
print("Sorted array: ", res)