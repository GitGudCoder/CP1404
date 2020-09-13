from prac_6.guitar_class import Guitar

my_guitar = Guitar("Ibanez", "Prestige RGT 220A", 2006, 3000)
print(my_guitar, "\n")

# Testing Class methods on my guitar
print("Using my_guitar.get_age() - Expected 14, got", my_guitar.get_age())
print("Using my_guitar.is_vintage() - Expected False, got", my_guitar.is_vintage())
# Testing Class methods on other guitar
other_guitar = Guitar("Gibson", "L-5 CES", 1922, 16035.40)
print("Using other_guitar.is_vintage() - Expected True, got", other_guitar.is_vintage())

