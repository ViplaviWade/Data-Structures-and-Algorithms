# Reverse words in a string

def reverseWords(s):
    words = s.strip().split()
    return ' '.join(reversed(words))

res = reverseWords(s="The sky is blue")
print(res)
res = reverseWords(s=" Hello World! ")
print(res)