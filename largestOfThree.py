num1 = int(input("Enter the first number\n"))
num2 = int(input("Enter the second number\n"))
num3 = int(input("Enter the third number\n"))

largest = num1

if largest < num2:
    largest = num2
if largest < num3:
    largest = num3

print(largest)