digit = 0
vowels = 0
consonants = 0
specialcharacter_and_whitespaces = 0
str = input("enter the string: ")

for i in range(0, len(str)):
    ch = str[i]
    if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):

        # To convert uppercase into lowercase
        
        ch = ch.lower()

        if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
            vowels += 1
        else:
            consonants += 1
    elif (ch >= '0' and ch<= '9'):
        digit += 1
    else:
        specialcharacter_and_whitespaces += 1

print("string:", str)
print("no. of digits string have:", digit)
print("no. of vowels string have:", vowels)
print("no. of consonants string have:", consonants)
print("no. of special characters and white spaces string have:", specialcharacter_and_whitespaces)
