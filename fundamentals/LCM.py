# GCD

num1 = int(input("Enter the First number : "))
num2 = int(input("Enter the Second number : "))
listofnum1 = []
listofnum2 = []

# Loop to get the factors of listofnum1
 
for j in range (1,num1+1):
  if num1 % j == 0:
      listofnum1.append(j)
print("Factors of numb1 :",listofnum1)

# Loop to get the factors of listofnum2
 
for j in range (1,num2+1):
  if num2 % j == 0:
      listofnum2.append(j)
print("Factors of numb2 :",listofnum2)

# Comparing the factors between two numbers with a formula
 
gcd = []
for x in listofnum1:
    if x in listofnum2:
        gcd.append(x)
print(f"The GCD of {num1} and {num2} is {gcd[-1]}")

# For LCM the calculation will be multiple of two number divided by gcd of both numbers
#Lcm = num1*num2 /gcd (num1,num2)

lcm = (num1 * num2) / gcd[-1]

print(f"The LCM of {num1} and {num2} is {lcm}")
