# Leetcode-14: Longest Common Prefix
# Input: ["flower", "flow", "flight"] → Output: "fl"

def longestCommonPrefix(strs):
    if not strs:
        print(strs)
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        i = 0
        while i < len(prefix) and i < len(s) and prefix[i] == s[i]:
            i += 1
        prefix = prefix[:i]
        if not prefix:
            break
    return prefix

prefix = longestCommonPrefix(strs= ["flower","flow","flight"])
print(prefix)
    