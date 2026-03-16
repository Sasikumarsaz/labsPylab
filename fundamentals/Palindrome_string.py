a = "mom"
b = len(a)
is_palindrome = True
for i in range (b//2):
    if a[i] != a[b - 1 - i]:
        is_palindrome = False
        break
if is_palindrome:
    print ("Is a palindrome")
else:
     print ("Is not a palindrome")
