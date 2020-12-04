#!/usr/bin/python

import sys, os, argparse
from itertools import combinations
import operator

def main(args):
    count_one = count_two = 0
    with open(args.file) as fd:
        nums = map(int, fd.read().splitlines())

        for a in combinations(nums, 2):
            if sum(a) == 2020:
                count_one = reduce(operator.mul, a, 1)
        for a in combinations(nums, 3):
            if sum(a) == 2020:
                count_two = reduce(operator.mul, a, 1)
    if args.one:
        print("Problem 1: %d" % count_one)
    if args.two:
        print("Problem 2: %d" % count_two)


if __name__ == "__main__":
    default_file = sys.argv[0].split("-")[0] + "-input.txt"
    ap = argparse.ArgumentParser(description="2020 Day 1 AOC")
    ap.add_argument("-1", "--one", action="store_true", help="Problem 1")
    ap.add_argument("-2", "--two", action="store_true", help="Problem 2")
    ap.add_argument("file", help="Input file", default=default_file, nargs="?")
    args = ap.parse_args()
    if not args.one and not args.two:
        args.one = args.two = True
    main(args)
    
