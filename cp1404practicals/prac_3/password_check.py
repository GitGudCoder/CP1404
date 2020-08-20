"""This is an example of user defined functions.
The inside functions are defined separately from the main to save more space and make the code easier to read"""


def get_password():
    """This function asks the user their password and returns the password"""
    psswrd = input("Please enter your password: >")
    return psswrd

def asterisk_printer(psswrd):
    """This function converts user password into asterisks and prints"""
    hidden_password = "*" * len(psswrd)
    print("Password: {}".format(hidden_password))
    return

def main():
    """Main function asks for password from user, checks that it meets a minimum length requirement,
    then (if password is valid,) prints the password as asterisks
    """
    minimum_password_length = 10
    password = get_password()

    while len(password) < minimum_password_length :
        print("\nPassword must be at least {} characters long".format(minimum_password_length))
        password = get_password()

    asterisk_printer(password)
#^^^ None of the above code^^^ actually "runs", it is defined

main() #<--- The whole code is placed inside of this nested main() function. The code "runs" from here


