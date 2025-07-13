# Permuatations in String: check if a string(all letters) are present in other string. Can be in any order

def checkInclusion(s1, s2):
    for i in range(len(s2)- len(s1)+1):
        str = s2[i:len(s1)+i]
        count = 0
        for ch in str:
            if ch in s1:
                count += 1
            if count == len(s1):
                return True
    return False
    
ans = checkInclusion(s1 = "ab", s2 = "eidbaooo")
print(ans)
ans = checkInclusion(s1 = "ab", s2 = "eidboaoo")
print(ans)