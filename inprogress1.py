def calc_Con():
    second_Cal = str(input("Would you like to continue. [Y/N]\n"))
    if second_Cal == "Y":
        calc()
    elif second_Cal == "y":
        calc()



def second_choice_int():
    symbol = str(input("+, -, /, *, ^, !!. \n "))
    num2 = float(input("What is the second number you would like to enter: \n"))
    if symbol == "+":
        print(num1 + num2)
        calc_Con()
    elif symbol == "-":
        print(num1 - num2)
        calc_Con()
    elif symbol == "/":
        print(num1 / num2)
        calc_Con()
    elif symbol == "*":
        print(num1 * num2)
        calc_Con()
    elif symbol == "^":
        print(num1 ** num2)
        calc_Con()



print("Hello and Welcome.")


def calc():
    num1 = float(input("What is the first number would you like to enter: "))
    second_Choice = str(input("Do you need to enter another number? [Y/N]\n"))

    if second_Choice == "Y":
        symbol = str(input("+, -, /, *, ^, !!. \n "))
        num2 = float(input("What is the second number you would like to enter: \n"))
        if symbol == "+":
            print(num1 + num2)
            calc_Con()
        elif symbol == "-":
            print(num1 - num2)
            calc_Con()
        elif symbol == "/":
            print(num1 / num2)
            calc_Con()
        elif symbol == "*":
            print(num1 * num2)
            calc_Con()
        elif symbol == "^":
            print(num1 ** num2)
            calc_Con()

    elif second_Choice == "y":
        symbol = str(input("+, -, /, *, ^, !!. \n "))
        num2 = float(input("What is the second number you would like to enter: \n"))
        if symbol == "+":
            print(num1 + num2)
            calc_Con()
        elif symbol == "-":
            print(num1 - num2)
            calc_Con()
        elif symbol == "/":
            print(num1 / num2)
            calc_Con()
        elif symbol == "*":
            print(num1 * num2)
            calc_Con()
        elif symbol == "^":
            print(num1 ** num2)
            calc_Con()
    elif second_Choice == "N":
        symbol = str(input("!!. \n "))
        if symbol == "!!":
            import math
            print(math.sqrt(num1))
            calc_Con()

    elif second_Choice == "n":
        symbol = str(input("!!. \n "))
        if symbol == "!!":
            import math
            print(math.sqrt(num1))
            calc_Con()


app = str(input("Type 1 to start. \n"))
if bool(app == "1"):
    num1 = float(input("What is the first number would you like to enter: "))
    second_Choice = str(input("Do you need to enter another number? [Y/N]\n"))

    if second_Choice == "Y":
        second_choice_int()

    elif second_Choice == "y":
        symbol = str(input("+, -, /, *, ^, !!. \n "))
        num2 = float(input("What is the second number you would like to enter: \n"))
        if symbol == "+":
            print(num1 + num2)
            calc_Con()
        elif symbol == "-":
            print(num1 - num2)
            calc_Con()
        elif symbol == "/":
            print(num1 / num2)
            calc_Con()
        elif symbol == "*":
            print(num1 * num2)
            calc_Con()
        elif symbol == "^":
            print(num1 ** num2)
            calc_Con()

    elif second_Choice == "n":
        symbol = str(input("!!. \n "))
        if symbol == "!!":
            import math

            print(math.sqrt(num1))
            calc_Con()
    elif second_Choice == "N":
        symbol = str(input("!!. \n "))
        if symbol == "!!":
            import math

            print(math.sqrt(num1))
            calc_Con()
