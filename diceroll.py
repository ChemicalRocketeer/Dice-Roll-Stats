"""
Let's say I make a bet with you that you will roll 2 dice, and I will predict 2 numbers,
and if you rolled either of the numbers that I predicted, then I win. What is the probability that I'll win?
This program aims to answer that question.
It rolls pairs of dice, simulates every possible prediction I might make, and counts
the number of times that one of the two predicted numbers is correct.
"""

import random

rollcount = 10000

print ("Rolling  " + str(rollcount) + " dice...")

random.seed()
rolls = [(random.randint(1, 6), random.randint(1, 6)) for i in range(rollcount)]

print("comparing dice...")

matches = 0

# make 2 predictions: a and b. For each possible value of a and b,
# go through the list of rolls and count how many times the prediction is correct.
for a in range(1, 7):
    for b in range(1, 7):
        # skip this iteration if the two prediction numbers are equal.
        # (you can't predict that the roll will have a 2 or a 2)
        if b != a:
            for roll in rolls:
                if roll[0] == a or roll[0] == b or roll[1] == a or roll[1] == b:
                    matches += 1

# 30 different predictions times the number of rolls = total comparisons
comparisons = 30 * len(rolls)
print("probability: " + str(matches / comparisons))
