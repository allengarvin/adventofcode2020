#!/usr/bin/python3

import sys, os, argparse, operator, re

def main(args):
    fd = open(args.file)
    nums = sorted([int(n, 2) for n in fd.read().translate(str.maketrans({"F":"0", "B":"1", "R":"1", "L":"0"})).splitlines()])
    if args.one:
        print("Problem 1: %d" % nums[-1])
    if args.two:
        print("Problem 2: %d" % list(set(range(nums[0], nums[-1])) - set(nums))[0])
        

if __name__ == "__main__":
    default_file = sys.argv[0].split("-")[0] + "-input.txt"
    ap = argparse.ArgumentParser(description="2020 Day 5 AOC: Binary boarding")
    ap.add_argument("-1", "--one", action="store_true", help="Problem 1")
    ap.add_argument("-2", "--two", action="store_true", help="Problem 2")
    ap.add_argument("file", help="Input file", default=default_file, nargs="?")
    args = ap.parse_args()
    if not args.one and not args.two:
        args.one = args.two = True
    main(args)
    
