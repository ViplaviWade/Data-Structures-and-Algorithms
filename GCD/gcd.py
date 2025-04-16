num1 = int(input("Enter first number: "))
num2 = int(input("Enter first number: "))
result = min(num1, num2)

while result:
    if num1 % result == 0 and num2 % result == 0:
        break
    result -= 1

print(f"Greatest common divisor of {num1} and {num2} is: {result}")