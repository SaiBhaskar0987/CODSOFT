def calculate(num1,num2,op):
    if op == "+":
        result = num1 + num2
        print("Result: ",result)
    elif op == "-":
        result = num1 - num2
        print("Result: ",result)
    elif op == "*":
        result = num1 * num2
        print("Result: ",result)
    elif op == "/":
        if num2 != 0:
            result = num1 / num2
            print("Result: ",result)
        else:
            print("Error", "Cannot divide by zero.")
            return
while True:
    num1 = float(input("Enter Your first number: "))
    num2 = float(input("Enter Your second number: "))
    op = input("Enter which Operation you world perform(+, -, *, /): ")

    calculate(num1,num2,op)

    enter = input("If You want to continue your calculation, If yes Enter 'Y' or 'N': ").lower()
    if enter == "y":
        continue
    else:
        break
        print("Thanks for using")
