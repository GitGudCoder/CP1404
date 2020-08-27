# INTERMEDIATE EXCERCISES
def main():
    perform_basic_list_operations()
    access = woefully_inadequate_security_checker()
    if access:
        print("Access granted")
    else:
        print("Access denied")


# 1. BASIC LIST OPERATIONS
def perform_basic_list_operations():
    user_inputs = int(input("Please enter the number of numbers you wish to enter: >>>"))
    numbers = []
    for i in range (0, user_inputs):
      numbers.append(int(input("Please enter number {}: ".format(i+1))))
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average number size is {}".format(sum(numbers) / user_inputs))


# 2. WOEFULLY INADEQUATE SECURITY CHECKER
def woefully_inadequate_security_checker():
    user = str(input("Please enter your username: >>>"))
    user_names = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    if user in user_names:
        return True
    else:
        return False


main()

