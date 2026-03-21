import re
word = "Apple" 
word1 = "orange"


with open("C:/Users/Sasik/Documents/file1test.txt","r") as inputfile:
    for line in inputfile:
        newline = line.replace(word, word1) #replace the word in the line
        print(newline)
