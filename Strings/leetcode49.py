# Group Anagrams

from collections import defaultdict

def groupAnagrams(strs):
    res = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        res[key].append(s)
    return list(res.values())

res = groupAnagrams(strs= ["eat","tea","tan","ate","nat","bat"])
print(res)