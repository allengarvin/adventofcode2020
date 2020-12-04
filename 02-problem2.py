#!/usr/bin/python

import sys, os, argparse

def main(args):
    fd = open(args.file)
    count_one = count_two = 0

    for line in fd:
        r, let, p = line.strip().split()
        let = let.strip(":")
        low, high = map(int, r.split("-"))
        if p.count(let) >= low and p.count(let) <= high:
            count_one += 1            
        num = 0
        if p[low-1] == let:
            num += 1
        if p[high-1] == let:
            num += 1
        if num == 1:
            count_two += 1

    if args.one:
        print("Problem 1: %d" % count_one)
    if args.two:
        print("Problem 2: %d" % count_two)

if __name__ == "__main__":
    default_file = sys.argv[0].split("-")[0] + "-input.txt"
    ap = argparse.ArgumentParser(description="2020 Day 2 AOC: Password philosophy")
    ap.add_argument("-1", "--one", action="store_true", help="Problem 1")
    ap.add_argument("-2", "--two", action="store_true", help="Problem 2")
    ap.add_argument("file", help="Input file", default=default_file, nargs="?")
    args = ap.parse_args()
    if not args.one and not args.two:
        args.one = args.two = True
    main(args)
    
