# Longest substring without repeating a character

def lengthOfLongestSubstring(s):
    start, end, max_length, seen = 0, 0, 0, set()
    for end in range(len(s)):
        while s[end] in seen:
            seen.remove(s[start])
            start += 1
        seen.add(s[end])
        max_length = max(max_length, end - start +1)
    return max_length

res = lengthOfLongestSubstring(s = "abcabcbb")
print(res)
res = lengthOfLongestSubstring(s = "bbbbb")
print(res)