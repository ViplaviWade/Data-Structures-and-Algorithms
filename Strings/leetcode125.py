# Leetcode-125: Valid Plaindrome
# Input= "A man, a plan, a canal: Panama" Output: True

def validPalindrome(s):
    left, right = 0, len(s)-1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

res = validPalindrome(s = "A man, a plan, a canal: Panama")
print(res)