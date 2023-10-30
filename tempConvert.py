# Main function
def convertTemp():
    print("TEMPERATURE CONVERTER\n")

    userChoice = input("What would you like to convert? Please input the corresponding number.\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n")
    if int(userChoice) == 1:
        celsius = input("\nConverting Celsius to Fahrenheit. Please input a number for Celsius to convert:\n")
        fahrenheit = (int(celsius) * 9/5) + 32
        print(celsius + " Celsius is equal to " + str(fahrenheit) + " Fahrenheit.\n")
    elif int(userChoice) == 2:
        fahrenheit = input("\nConverting Fahrenheit to Celsius. Please input a number for Fahrenheit to convert:\n")
        celsius = (int(fahrenheit) - 32) * 5/9
        print(fahrenheit + " Fahrenheit is equal to " + str(celsius) + " Celsius.\n")

# Start
convertTemp()