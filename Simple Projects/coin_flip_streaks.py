# find out how often a streak of six heads/tails comes
# up in randomly generated lost of heads and tails.

import random
numberOfStreaks = 0
coinList = []

for experimentNum in range(10000):
    for i in range(100):
        if random.randint(0,1)==0:
            coinList.append("T")
        else:
            coinList.append("H")

    streak = 0
    for i in range(len(coinList)):
        if i == 0:
            pass
        elif coinList[i] == coinList[i-1]:
            streak += 1
        else:
            streak = 0

        if streak == 6:
            numberOfStreaks += 1
    coinList = []
print("Chance of streak:  %s%%" % (numberOfStreaks / 100))
