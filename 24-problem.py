#!/usr/bin/python

import sys, os, argparse, operator, re
from parse import parse

def tuple_add(t1, t2):
    return tuple(map(lambda i, j: i + j, t1, t2))

def parse_line(h):
    dirs = []
    i = 0
    while i < len(h):
        if h[i:i+2] in ["ne", "se", "sw", "nw"]:
            dirs.append(h[i:i+2])
            i += 2
        else:
            dirs.append(h[i])
            i += 1
    return dirs

def main(args):
    floor = dict()
    tiles = [parse_line(x.strip()) for x in open(args.file)]
    shifts = { "ne" : (1,-1), "se" : (1,1), "nw" : (-1,-1), "sw" : (-1,1), "w" : (-2,0), "e" : (2, 0) }

    for t in tiles:
        x, y = reduce(lambda x,y: tuple_add(x,y), [shifts[x] for x in t])
        floor[(x,y)] = 1 - floor.get((x,y), 0)
    
    print("Problem 1: {0}".format(floor.values().count(1)))

    for day in range(1, 101):
        new_floor = dict()
        for x,y in floor.keys():
            new_floor[(x,y)] = floor.get((x,y), 0)
            neighbors = {tuple_add((x,y), p) : floor.get(tuple_add((x,y), p), 0) for p in shifts.values()}
            new_floor.update(neighbors)
    
        for i, j in new_floor:
            if new_floor[(i,j)]:
                black_count = [ floor.get(tuple_add((i,j), p), 0) for p in shifts.values() ].count(1)
                if black_count == 0 or black_count > 2:
                    new_floor[(i,j)] = 0
            else:
                if [ floor.get(tuple_add((i,j), p), 0) for p in shifts.values() ].count(1) == 2:
                    new_floor[(i,j)] = 1
        floor = new_floor
    
        #print("Day {0}: {1}".format(day, floor.values().count(1)))
    print("Problem 2: {0}".format(floor.values().count(1)))

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2020 Day {0} AOC: Lobby Layout".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
