# Permuatations in String: check if a string(all letters) are present in other string. Can be in any order

from collections import Counter

def checkInclusion(s1: str, s2: str):
    c1 = Counter(s1)
    for i in range(len(s2)-len(s1)+1):
        if Counter(s2[i:len(s1)+i]) == c1:
            return True
    return False
   
ans = checkInclusion(s1 = "ab", s2 = "eidbaooo")
print(ans)
ans = checkInclusion(s1 = "ab", s2 = "eidboaoo")
print(ans)