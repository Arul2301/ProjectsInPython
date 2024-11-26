operator = input("Enter the operator( + - * /): ")
Num1 = float(input("Enter the num1 : "))
Num2 = float(input("Enter the num2: "))

if(operator == "+"):
    result = Num1 + Num2
    print(result)
elif(operator == "-"):
    result = Num1 - Num2
    print(result)
elif(operator == "*"):
    result = Num1 * Num2
    print(result)
elif(operator == "/"):
    result = Num1 / Num2
    print(round(result, 2))
else:
    print(f"{operator} is invalid operator")
    