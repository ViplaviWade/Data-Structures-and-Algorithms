# Valid Anagram

def isAnagram(s, t):
    hash = {}
    for char in s:
        if char in hash:
            hash[char] += 1
        else:
            hash[char] = 1
    for char in t:
        if char in hash:
            hash[char] -= 1
        else:
            return False
    for val in hash.values():
        if val != 0:
            return False
    return True

print(isAnagram(s = "anagram", t = "nagaram"))
print(isAnagram(s = "rat", t = "car"))