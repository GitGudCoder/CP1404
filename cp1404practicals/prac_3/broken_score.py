# BROKEN_SCORE (mk2)

from random import randint

def score_decoder(score):
    """This function takes in a score (number) and returns a mark (string)"""
    if score < 0 or score > 100:
        mark = "Invalid score"
    elif 50 <= score < 90:
        mark = "passable"
    elif score >= 90:
        mark = "excellent"
    else:
        mark = "bad"
    return mark


def main():
    """prompts the user for a score and assesses it, then generates a random number and assesses that"""
    score = float(input("Enter score: >"))
    result = score_decoder(score)
    print(result)

    # Part C? not sure if correct. Generates random number and assesses it
    score = randint(-10, 110)
    print(score)
    result = score_decoder(score)
    print(result)


main()
