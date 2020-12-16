#!/usr/bin/python

import sys, os, argparse, operator, re, string

def valid_height(hgt):
    h, unit = hgt[:-2], hgt[-2:]
    if h.isdigit() and ((unit == "cm" and 150 <= int(h) <= 193) or (unit == "in" and 59 <= int(h) <= 76)):
        return True
    return False

def main(args):
    validation = {
        "byr" : lambda x: x.isdigit() and 1920 <= int(x) <= 2002,
        "iyr" : lambda x: x.isdigit() and 2010 <= int(x) <= 2020,
        "eyr" : lambda x: x.isdigit() and 2020 <= int(x) <= 2030,
        "hgt" : valid_height,
        "hcl" : lambda x: len(x) == 7 and x[0] == "#" and reduce(operator.and_, [i in string.hexdigits for i in list(x[1:])]),
        "ecl" : lambda x: x in [ "amb", "blu", "brn", "gry", "grn", "hzl", "oth" ],
        "pid" : lambda x: x.isdigit() and len(x) == 9,
        "cid" : lambda x: True
    }
    records = [p.replace("\n", " ") for p in open(args.file).read().split("\n\n")]
    count_one = count_two = 0
    for p in records:
        passport = dict([x.split(":") for x in p.split()])
        if len(passport) == 8 or (len(passport) == 7 and "cid" not in passport):
            count_one += 1

            if reduce(operator.and_, [validation[k](v) for k, v in passport.iteritems()]):
                count_two += 1
    print("Problem 1: %d" % count_one)
    print("Problem 2: %d" % count_two)

if __name__ == "__main__":
    default_file = sys.argv[0].split("-")[0] + "-input.txt"
    ap = argparse.ArgumentParser(description="2020 Day 4 AOC: Passport processing")
    ap.add_argument("file", help="Input file", default=default_file, nargs="?")
    main(ap.parse_args())
