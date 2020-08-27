from random import randint

number_of_quick_picks = int(input("How many quick picks? >>>"))
quick_picks = []
for i in range(0, number_of_quick_picks):
    line_numbers = []
    line_numbers.append(randint(1,45))
    for n in range(0, 5):
        random_number = randint(1, 45)
        while random_number in line_numbers:
            random_number = randint(1,45)
        line_numbers.append(random_number)
    quick_picks.append(line_numbers)
    quick_picks[i].sort()
    print("{:>2} {:>2} {:>2} {:>2} {:>2} {:>2}".format(quick_picks[i][0], quick_picks[i][1], quick_picks[i][2],
                                                       quick_picks[i][3], quick_picks[i][4], quick_picks[i][5]))


