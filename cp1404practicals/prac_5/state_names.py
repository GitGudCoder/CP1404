"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# Already was formatted according to PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
# Old printout
# print(CODE_TO_NAME)

# New printout
for state_code, state_name in CODE_TO_NAME.items():
    print("{:^3} is {}".format(state_code, state_name))

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()


