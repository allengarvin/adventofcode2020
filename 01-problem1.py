#!/usr/bin/python

import sys, os, argparse
from itertools import combinations
from operator import mul

def main(args):
    nums = map(int, open(args.file).readlines())

    for n in [2,3]:
        print "Problem {0}: {1}".format(n-1, reduce(mul, filter(lambda x: sum(x) == 2020, combinations(nums, n))[0]))

if __name__ == "__main__":
    default_file = sys.argv[0].split("-")[0] + "-input.txt"
    ap = argparse.ArgumentParser(description="2020 Day 1 AOC: Report repair")
    ap.add_argument("file", help="Input file", default=default_file, nargs="?")
    args = ap.parse_args()
    main(args)
    
