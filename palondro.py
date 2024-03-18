word = "anzil"
word= input("Enter your name: ")
print(" name",word)
flag = True
length = len(word)

for i in range(length //2):
    if word[i] != word[length - 1 - i]:
        flag = False
        break

if flag:
    print("is palindrome")
else:
    print("not palindrome")
