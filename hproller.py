#!/usr/bin/env python3

import random
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('hit_die', help="Your Character's hit die")
    parser.add_argument('level', help="Your Character's level")
    parser.add_argument('cons', help="Your Character's CONS modifier")
    args = parser.parse_args()
    hit_die = int(args.hit_die)
    level = int(args.level)
    cons = int(args.cons)

    hp = hit_die + cons
    for i in range(level-1):
        roll = random.randint(1, hit_die)
        hp += (roll + cons)
    print(hp)


if __name__ == "__main__":
    main()