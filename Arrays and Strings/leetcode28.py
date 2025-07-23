# Leetcode-28: Find the Index of the First occurence in a String
# Input: haystack = "sadbutsad", needle = "sad" Output: 0 

def strStr(haystack, needle):
    for i in range(len(haystack)- len(needle) - 1):
        if haystack[i:len(needle)+i] == needle:
            return i
    return -1
    
num = strStr(haystack = "sadbutsad", needle = "sad")
if num == -1:
    print("The substring does not occur in the string")
else:
    print("The substring occurs in the String at index: ", num)