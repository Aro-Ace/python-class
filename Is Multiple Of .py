print('welcome! choose two numbers and i will tell you if one is a multiple of the other.')
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 % num2 == 0:
    print(f"{num1} is a multiple of {num2}.")
    print(f"{num1} is {num1/num2} times {num2}.")
elif num2 % num1 == 0:
    print(f"{num2} is a multiple of {num1}.")
    print(f"{num2} is {num2/num1} times {num1}.")
else:
    print("Neither number is a multiple of the other.")
