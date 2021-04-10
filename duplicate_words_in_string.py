a = input("enter the string: ")
a = a.lower()
words = a.split(" ")
print("duplicates words in a string: ")
for i in range(0 , len(words)):
    count = 1
    for j in range(i + 1 , len(words)):
        if(words[i] == words[j]):
            count = count + 1
            words[j] = "0"
    if(count > 1 and words[i] != "0"):
        print(words[i])
