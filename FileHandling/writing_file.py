import re
word = r"here$" # to print the lines that end with "here" 
word1 = r"^some" # to print the lines that start with "some"



with open("C:/Users/Sasik/Documents/file1test.txt","r") as inputfile, open("C:/Users/Sasik/Documents/newfile.txt","w") as outputfile:
    for line in inputfile:
        if re.search(word, line, re.IGNORECASE):    # to ignore the case sensitivity
            print(line)
            outputfile.write(line)
