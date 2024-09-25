num1= float(input("enter first number:"))
num2 = float(input("enter second number:"))
operation = input("enter symbol (add,subtract,times,divide:)")

if operation == 'add': 
    print("result:", num1 + num2)
elif operation == 'subtract':
    print("result:", num1 - num2)
elif operation == 'times':
    print("result:", num1 * num2)   
elif operation == 'divide':
    print("result:", num1 / num2)      