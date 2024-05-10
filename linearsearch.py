def linear_search(key, lst):
    cnt=0
    for i in lst:
       cnt+=1
       if i == key:
           print(f"The number {key} is found at position {cnt}") 

n = int(input("Enter number of elements : "))
lst = []
for i in range(n):
    inp = int(input(f"Enter element number {i} :"))
    lst.append(inp)

key = int(input("Enter number to search : "))

linear_search(key, lst)