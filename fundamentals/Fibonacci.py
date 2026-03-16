num = int(input("Enter the number of iteration: "))
val1 = 0
val2 = 1
print(val1)
print(val2)
for x in range (0,num-2):
    val3 = val1+val2
    val1=val2
    val2=val3
    print(val3)
