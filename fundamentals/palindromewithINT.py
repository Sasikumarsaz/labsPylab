num = 12323
num1 = num
reverse = 0

while num != 0:
    reverse = reverse * 10 + (num % 10 )
    num = num // 10
    #print (num)
    #print (reverse)
if reverse == num1:
    print(" Is a palindrome")
else:
    print("Is not a palindrome")
