#!/usr/bin/env python3

import random

def main():
    stats = []
    for i in range(6):
        dice = []
        for j in range(4):
            dice.append(random.randint(1,6))
        dice.sort(reverse=True)
        stat = 0
        for die in dice[:3]:
            stat += die
        stats.append(stat)
    stats.sort(reverse=True)
    print(stats)


if __name__ == "__main__":
    main()