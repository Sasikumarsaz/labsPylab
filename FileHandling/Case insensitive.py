import re
word = "iphone"

with open("C:/Users/Sasik/Documents/file1test.txt", "r") as inputfile:
    for line in inputfile:
        if re.search(word, line, re.IGNORECASE):    # to ignore the case sensitivity
            print(line)
