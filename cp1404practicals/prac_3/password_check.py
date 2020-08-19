"""This is an example of defining user functions.
The inside functions are defined separately from the main to save more space"""

#Define the function that changes password to *****s
def get_password(psswrd):
    password_length = len(psswrd)
    #a global variable was needed to use variable in other function (return command did not work)
    global hidden_password
    hidden_password = "*" * (password_length)
    #print("Password: {}".format(hidden_password))<-- print was commented out so that password can only be printed if passlen>=6

#Defines the main function. In this case prompting the user for a password. The get_password function converts passord to stars and prints
#The outer main funtion deals with the case of having less than 6 characters. It loops util the password length is >= 6
def main():
    password = input("Please enter your password: >>>")
    get_password(password)

    while len(hidden_password) <6 :
        print("\nPassword must be at least 6 characters long")
        password = input("Please enter your password: >>>")
        get_password(password)

    print("\nPassword: {}".format(hidden_password))

#^^^ None of the above code^^^ actually "runs", it is a local function reference for the code below.

main() #<--- The whole code is placed inside of this nested main() function.


