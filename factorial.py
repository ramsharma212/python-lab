n = int(input("enter the positive number"))
fact = 1
while n > 0:
    fact *= n
    n -= 1
print(f'factorial of the number is {fact}')
