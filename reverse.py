num=int(input("enter the number"))
revs_number = 0
while (num > 0):
    a = num % 10
    revs_number = (revs_number * 10) + a
    num = num // 10
print(f'the reverse number is {revs_number}')
