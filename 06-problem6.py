#!/usr/bin/python

import sys, os, argparse, operator, re

def main(args):
    if args.one:
        answers1 = [set(x.replace("\n", "")) for x in open(args.file).read().split("\n\n")]
        print("Problem 1: %d" % sum(map(lambda x: len(set(x)), answers1)))
    if args.two:
        answers2 = [map(set, x.split()) for x in open(args.file).read().split("\n\n")]
        print("Problem 2: %d" % sum([len(reduce(operator.and_, x)) for x in answers2]))
    

if __name__ == "__main__":
    default_file = sys.argv[0].split("-")[0] + "-input.txt"
    ap = argparse.ArgumentParser(description="2020 Day 6 AOC: Custom customs")
    ap.add_argument("-1", "--one", action="store_true", help="Problem 1")
    ap.add_argument("-2", "--two", action="store_true", help="Problem 2")
    ap.add_argument("file", help="Input file", default=default_file, nargs="?")
    args = ap.parse_args()
    if not args.one and not args.two:
        args.one = args.two = True
    main(args)
    
