#!/usr/bin/python

import sys, os, argparse, operator, re

def valid_height(hgt):
    h, unit = hgt[:-2], hgt[-2:]
    if h.isdigit() and ((unit == "cm" and int(h) in range(150, 193+1)) or (unit == "in" and int(h) in range(59, 76+1))):
        return True
    return False

def main(args):
    validation = {
        "byr" : lambda x: x.isdigit() and int(x) in range(1920, 2002+1),
        "iyr" : lambda x: x.isdigit() and int(x) in range(2010, 2020+1),
        "eyr" : lambda x: x.isdigit() and int(x) in range(2020, 2030+1),
        "hgt" : valid_height,
        "hcl" : lambda x: len(x) == 7 and re.search("^#[0-9a-f]*$", x) and True,
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
    if args.one:
        print "Problem 1:", count_one
    if args.two:
        print "Problem 2:", count_two

if __name__ == "__main__":
    default_file = sys.argv[0].split("-")[0] + "-input.txt"
    ap = argparse.ArgumentParser(description="2020 Day 4 AOC: Passport processing")
    ap.add_argument("-1", "--one", action="store_true", help="Problem 1")
    ap.add_argument("-2", "--two", action="store_true", help="Problem 2")
    ap.add_argument("file", help="Input file", default=default_file, nargs="?")
    args = ap.parse_args()
    if not args.one and not args.two:
        args.one = args.two = True
    main(args)
    
