from prac_6.guitar_class import Guitar


def main():
    print("My guitars!")
    guitars = []
    make = str(input("Make: >")).title()
    while make != "":
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
        make = str(input("Make: >")).title()

    print("These are my guitars")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(Vintage)"
        print(f"Guitar {i}: {guitar}, {vintage_string}")


main()
