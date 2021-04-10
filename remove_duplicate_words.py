a = input("enter the string: ")
b = a.split()
k = []
for i in b:
    if(a.count(i) > 1 and (i not in k) or a.count(i) == 1):
        k.append(i)
print(' '.join(k))
