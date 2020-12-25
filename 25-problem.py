#!/usr/local/bin/python3.7

import sys, os, argparse

def transform(subject, keys, setloops):
    loops = [None] * len(keys)
    val = cnt = 1
    while None in loops:
        val = (val * subject) % 20201227
        if setloops:
            if cnt == setloops:
                return val
        else:
            for i, l in enumerate(loops):
                if l == None and val == keys[i]:
                    loops[i] = cnt
        cnt += 1
    return min(loops), keys[1 - loops.index(min(loops))]
        
def main(args):
    keys = [int(n) for n in open(args.file)]

    m, k = transform(7, keys, False)
    print("Part 1: {0}".format(transform(k, [None], m)))
    
if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2020 Day {0} AOC: Combo Breaker".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
