#!/usr/bin/python

import sys, os, argparse, operator

def treecount(map, slope):
    y = x = 0
    side = len(map[0])
    count = 0
    
    while True:
        y += slope[0]
        x = (x + slope[1]) % side
        if y >= len(map):
            break
        count += map[y][x]
    return count
        

def main(args):
    fd = open(args.file)
    map = []
    for line in fd:
        row = [1 if x == "#" else 0 for x in list(line.strip())]
        map.append(row)

    if args.one:
        print("Problem 1: %d" % treecount(map, (1, 3)))
    if args.two:
        print("Problem 2: %d" % reduce(operator.mul, [treecount(map, (y,x)) for y, x in (1,1), (1,3), (1,5), (1,7), (2,1)]))
            

if __name__ == "__main__":
    default_file = sys.argv[0].split("-")[0] + "-input.txt"
    ap = argparse.ArgumentParser(description="2020 Day 3 AOC: Toboggan trajectory")
    ap.add_argument("-1", "--one", action="store_true", help="Problem 1")
    ap.add_argument("-2", "--two", action="store_true", help="Problem 2")
    ap.add_argument("file", help="Input file", default=default_file, nargs="?")
    args = ap.parse_args()
    if not args.one and not args.two:
        args.one = args.two = True
    main(args)
    
