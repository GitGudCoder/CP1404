"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for i in range(number_of_months):
        income = float(input("Enter income for month {}: ".format(i+1)))
        incomes.append(income)

    print_report(incomes, number_of_months)


def print_report(incomes, number_of_months):
    """Prints incomes over input months with running total"""
    print("\nIncome Report\n-------------")
    running_total = 0
    for i in range(number_of_months):
        running_total = sum(incomes[0:i + 1])
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(i + 1, incomes[i], running_total))


main()