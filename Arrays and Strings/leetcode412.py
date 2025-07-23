# FizzBuzz Classic Problem

from random import randint

def fizzBuzz(n):
    ans = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            ans.append("FizzBuzz")
        elif i % 3 == 0:
            ans.append("Fizz")
        elif i % 5 == 0:
            ans.append("Buzz")
        else:
            ans.append(str(i))
    return ans

ans = fizzBuzz(n = randint(1, 10))
for i in ans:
    print(i)