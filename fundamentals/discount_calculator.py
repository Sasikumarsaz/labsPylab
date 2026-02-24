# This is a simple discount calculator

age = int(input ("Enter your age= "))
Price =int(input("Price: "))
Total = Price * 0.18
#print (Total)

if age >= 50:
    print (Total)
elif age <=49:
    Student = input ("Are you student (yes/no): ")
    if Student in ['yes']:
                StudentDiscount = Total * 0.15
                Total -= StudentDiscount
                print ("Student discount added: ", Total)
    else:
                print ("No student discount: ", Total)
else:
    print("Age is greater than 50,No Student discount: ", Total)
