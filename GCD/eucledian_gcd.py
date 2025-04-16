def gcd(a, b):
    if a==0:
        return b
    if b==0:
        return a
    if a==b:
        return a
    if a>b:
        return gcd(a-b, b)
    return gcd(a, b-a)

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

res = gcd(num1, num2)
print(f"GCD of {num1} and {num2} is {res}")