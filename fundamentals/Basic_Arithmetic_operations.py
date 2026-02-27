a = int(input("Enter value A: "))
b = int(input("Enter value B: "))

solution_1 = a / b
solution_2 = a // b
solution_3 = a % b
solution_4 = a ** b

print(f"Div of = {solution_1:.2f}\nFloor division of = {solution_2}\nModulus of = {solution_3}\nExponentiation of = {solution_4}\n")

# or we can use round(soltuion_1,2) while printing Div value to restrict decimal to 2 f
