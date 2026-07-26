try:
    choosen_number1 = int(input("Input the first number"))
    choosen_number2 = int(input("Input the second number"))
    result = choosen_number1 / choosen_number2
    print(result)
    print("Thank you for using our program!")
except ValueError:
    print("Please input a number!")
except ZeroDivisionError:
    print("Divison by zero is impratical")