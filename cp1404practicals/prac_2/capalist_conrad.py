"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
import random

#Breaking Python naming conventions is bad.
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.00
MAX_PRICE = 100.00
INITIAL_PRICE = 10.00
#For real^^^

price = INITIAL_PRICE

#Makes/overwrites a write only file called "OUTPUT_FILE"
out_file = open("output_file.txt", "w")

#Initialises a day counter. Day will increment at end of while loop
day_number = 1
#The first message prints outside of the loop
#All printed strings are saved to output_file
print("Starting price: ${:.2f}".format(INITIAL_PRICE),file=out_file)

while price >= MIN_PRICE and price <= MAX_PRICE:

    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print("On day {} price is:${:,.2f}".format(day_number,price),file=out_file)

    #Last thing to do is index the day
    day_number += 1

if price - 60 < 0:
    print("You ran out of money on day {}".format(day_number),file=out_file)
else:
    print("Quit while you're ahead...",file=out_file)

#Close the file
out_file.close