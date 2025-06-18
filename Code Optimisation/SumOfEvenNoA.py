def sum_even_numbers(numbers):
    return sum(x for x in numbers if x % 2 == 0)

res = sum_even_numbers(numbers = [1,2,3,4,5])
print(res)