num1= float(input ("Enter a number: "))
num2 = float(input ("Enter another number: "))
operation = input("Choose +, -, * or /: ")
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    result = "Invalid operation"
print(result)
