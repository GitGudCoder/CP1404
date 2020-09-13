from prac_6.guitar_class import Guitar


def main():
    print("My guitars!")
    guitars = []
    while True:
        make = str(input("Make: >")).title()
        if make == "":
            break
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

    print("These are my guitars")
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")


main()
