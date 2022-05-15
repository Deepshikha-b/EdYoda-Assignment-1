word = input("Enter the word here: ")
word_len = len(word)
i = word_len - 1
print("It's  reverse is: ",end="")
while i >= 0:
    print(word[i] , end = "")
    i -= 1