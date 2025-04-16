n = int(input("Enter a number:"))
t = n
sum=0
while n > 0:
    rem = n % 10
    sum = sum*10 + rem
    n = n // 10

if sum == t:
    print(f"{t} is a Palindrome number")
else:
    print(f"{t} is not a Palindrome number")