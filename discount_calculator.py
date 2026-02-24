# This is a simple discount calculator

age = int(input ("Enter your age= "))
Price =int(input("Price: "))
Total = Price * 0.18
#print (Total)

if age <=49:
    Student = input ("Are you student (yes/no): ")
    if Student in ['yes']:
                StudentDiscount = Total * 0.15
                Total -= StudentDiscount
                print ( f"Student discount added: {Total}")
    else:
                print (f"No student discount: {Total}")
else:
    print( f"Age= {age} which is greater than 49, Hence No student discount applied. Total is {Total}" )
