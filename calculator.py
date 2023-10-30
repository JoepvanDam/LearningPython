# Main function
def calculator():
    print("\nCALCULATOR")
    firstNum = int(input("Input the first number\n"))
    operation = input("\nInput your operation (+, -, /, *, **, or %)\n")
    secondNum = int(input("\nInput the second number\n"))
    
    result = None
    if operation == "+":
        result = firstNum + secondNum
    elif operation == "-":
        result = firstNum - secondNum
    elif operation == "/":
        result = firstNum / secondNum
    elif operation == "*":
        result = firstNum * secondNum
    elif operation == "**":
        result = firstNum ** secondNum
    elif operation == "%":
        result = firstNum % secondNum

    print("\n" + str(firstNum) + " " + operation + " " + str(secondNum) + " = " + str(result))

    repeat = input("\nWould you like another calculation? Y/N\n")
    if repeat == "Y":
        calculator()
    else:
        print("\n")
        return
    
# Start
calculator()