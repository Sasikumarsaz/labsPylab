word = input("Enter the word : ")
while True :
    if len(word) < 5 :
        word = input("Enter the word more than 5 letters: ")
    elif len(word) > 5 :
        print("word length :",len(word))
        x = int(input("Where the split should happen : "))
        print(word[x:])
        break
