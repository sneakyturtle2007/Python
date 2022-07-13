valueba = 0

def app_choice():
    starting_input = input("Calculator, TicTacToe. Input below.\n")
    if starting_input == "Calculator":
        execfile('inprogress1.py')
    elif starting_input == "calculator":
        execfile('inprogress1.py')
    elif starting_input == "T":
        execfile('scratch.py')


def password_choice():
    starting_input = input("Calculator(1). Input below.\n")
    if starting_input == "1":
        execfile('inprogress1.py')

    elif starting_input == "T":
        execfile('scratch.py')
    else:
        var = valueba + 1
        print("That is not a valid input")
        while var == 1:
            app_choice()


def execfile(any):
    if any == 'inprogress1.py':
        import inprogress1
    elif any == 'scratch.py':
        import scratch


name = str(input("Hi what is your name.\n"))
password = input("Hi " + name + " could you please enter the password down below.\n")

if bool(password == "help"):
    password_choice()
else:
    while password != "help":
        print("Wrong Password.\n")
        password = input("Hi " + name + " could you please enter the password down below.\n")
    password_choice()
