#!/usr/bin/python

import sys, os, argparse, operator, re
from parse import parse
import numpy as np

def tuple_add(t1, t2):
    return tuple(map(lambda i, j: i + j, t1, t2))

def rotate(pos, deg):
    th = np.radians(deg)

    py, px = pos
    qx = np.rint(np.cos(th) * px - np.sin(th) * py)
    qy = np.rint(np.sin(th) * px + np.cos(th) * py)
    # print "ROT", pos, "rotated", deg, "->", (qy, qx)
    return (int(qy), int(qx))

def main(args):
    dirs = [(0,1), (-1,0), (0,-1), (1,0)]
    current_dir = 0
    pos = (0,0)

    actions = [(a[0],int(a[1:].strip())) for a in open(args.file).readlines()]
    for a, n in actions:
        if a == "N": pos = tuple_add(pos, (-n, 0))
        if a == "S": pos = tuple_add(pos, (n, 0))
        if a == "E": pos = tuple_add(pos, (0, n))
        if a == "W": pos = tuple_add(pos, (0, -n))
        if a == "F": pos = tuple_add(pos, (dirs[current_dir][0] * n, dirs[current_dir][1] * n))
        if a == "L": current_dir = (current_dir + n / 90) % 4
        if a == "R": current_dir = (current_dir - n / 90) % 4
        #print a, n, current_dir, pos
    print("Problem 1: %d" % sum(map(abs, pos)))

    pos = (0,0)
    current_dir = 0
    waypoint = (-1, 10)

    for a, n in actions:
        if a == "N": waypoint = tuple_add(waypoint, (-n, 0))
        if a == "S": waypoint = tuple_add(waypoint, (n, 0))
        if a == "E": waypoint = tuple_add(waypoint, (0, n))
        if a == "W": waypoint = tuple_add(waypoint, (0, -n))

        if a == "F": pos = tuple_add(pos, (waypoint[0] * n, waypoint[1] * n))
        if a == "L": waypoint = rotate(waypoint, -n)
        if a == "R": waypoint = rotate(waypoint, n)
        # print a, n, "pos=", pos, "waypoint=", waypoint

    print("Problem 2: %d" % sum(map(abs, pos)))
        #print a, n, current_dir, pos, waypoint
        
if __name__ == "__main__":
    default_file = sys.argv[0].split("-")[0] + "-input.txt"
    ap = argparse.ArgumentParser(description="2020 Day X AOC: Rain Risk")
    ap.add_argument("-1", "--one", action="store_true", help="Problem 1")
    ap.add_argument("-2", "--two", action="store_true", help="Problem 2")
    ap.add_argument("file", help="Input file", default=default_file, nargs="?")
    args = ap.parse_args()
    if not args.one and not args.two:
        args.one = args.two = True
    main(args)
    
