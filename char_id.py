ch=input("enter the character")
if ch.islower():
    print("ch is lowercase")
elif ch.isupper():
    print("ch is uppercase")
elif ch.isdigit():
    print("ch is digit")
else:
    print("ch is special character")
