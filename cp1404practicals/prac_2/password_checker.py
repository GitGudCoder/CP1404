"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

#Who keeps putting upper case names in here?
MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARS_REQUIRED = True
#Each one of these could have been done with ordinals
#Assigning a string to each is easier
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
lower_case_letter = "abcdefghijklmnopqrstuvwxyz"
upper_case_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
allnumbers = "0123456789"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # TODO: if length is wrong, return False

    #Tests if password is too long or short
    if len(password) < 5 or len(password) > 15:
       return False
    else:
        #Initialise count of each character type
        count_lower = 0
        count_upper = 0
        count_digit = 0
        count_special = 0

        #Cycles through each letter in word and searches for each character type then updates a tally
        #(Using Boolean values may be inefficient)
        for i in range(len(password)):
            #upper case search
            upper_boolean = password[i] in upper_case_letter
            if upper_boolean == True:
                count_upper +=1
            else:#lower case search
                lower_boolean = password[i] in lower_case_letter
                if lower_boolean == True:
                    count_lower +=1
                else:#Number search
                    digit_boolean = password[i] in allnumbers
                    if digit_boolean == True:
                        count_digit +=1
                    else:#Special character search
                        special_char_boolean = password[i] in SPECIAL_CHARACTERS
                        if special_char_boolean == True:
                            count_special +=1

    #If ALL character type count requirements are met, function returns true.
    if count_special >=1 and count_digit >=1 and count_lower >=1 and count_upper >=1:
        return True
    #If all conditions are NOT met, function returns false
    else:
        return False


main()