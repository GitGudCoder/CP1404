from prac_6.guitar_class import Guitar


def main():
    print("My guitars!")
    guitars = []
<<<<<<< HEAD
    make = str(input("Make: >")).title()
    while make != "":
=======
    while True:
        make = str(input("Make: >")).title()
        if make == "":
            break
>>>>>>> c14e2dba14518c01a96586aaedebc22762e60799
        model = str(input("Model: >")).title()
        year = ""
        while year == "":
            try:
                year = int(input("Year: >"))
            except ValueError:
                print("Year input must be an integer")
        cost = ""
        while cost == "":
            try:
                cost = float(input("Cost: >"))
            except ValueError:
                print("Cost input must be a number")
        new_guitar_entry = Guitar(make, model, year, cost)
        guitars.append(new_guitar_entry)
<<<<<<< HEAD
        make = str(input("Make: >")).title()

    print("These are my guitars")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(Vintage)"
        print(f"Guitar {i}: {guitar}, {vintage_string}")
=======

    print("These are my guitars")
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")
>>>>>>> c14e2dba14518c01a96586aaedebc22762e60799


main()
