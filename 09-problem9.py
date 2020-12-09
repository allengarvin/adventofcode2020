#!/usr/bin/python

import sys, os, argparse, operator, re
import itertools

def main(args):
    lines = [int(x.strip()) for x in open(args.file).readlines()]

    for n in range(args.queue, len(lines)):
        prev = lines[0 if n - args.queue < 0 else n - args.queue:n]
        sums = [x+y for x, y in itertools.combinations(prev, 2)]
        if lines[n] not in sums:
            print("Problem 1: %d" % lines[n])
            break

    for i in range(n-1):
        for j in range(i+1,n):
            if lines[n] == sum(lines[i:j]):
                print("Problem 2: %d" % sum(sorted(lines[i:j])[::j-i-1]))


                

if __name__ == "__main__":
    default_file = sys.argv[0].split("-")[0] + "-input.txt"
    ap = argparse.ArgumentParser(description="2020 Day 9 AOC: Encoding error")
    ap.add_argument("-1", "--one", action="store_true", help="Problem 1")
    ap.add_argument("-2", "--two", action="store_true", help="Problem 2")
    ap.add_argument("-q", "--queue", help="Number for day-9-queue", type=int, default=25)
    ap.add_argument("file", help="Input file", default=default_file, nargs="?")
    args = ap.parse_args()
    if not args.one and not args.two:
        args.one = args.two = True
    main(args)
    
