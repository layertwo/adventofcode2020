#!/usr/bin/env python3

import re


def get_passports(data):
    """
    get passports from file
    """
    passports = []
    passport = {}
    for idx, line in enumerate(data):
        if not line:
            passports.append(passport)
            passport = {}

        passport.update(dict(item.split(':') for item in line.split()))

        if idx + 1 == len(data):
            passports.append(passport)
    return passports


def valid_passport1(passport):
    """
    part 1: passport validation
    """
    _keys = ['byr', 'ecl', 'eyr', 'hgt', 'hcl', 'iyr', 'pid']
    return all(k in passport for k in _keys)


def valid_passport2(passport):
    """
    day 2 passport validation
    """
    _keys = ['byr', 'ecl', 'eyr', 'hgt', 'hcl', 'iyr', 'pid']
    if not all(k in passport for k in _keys):
        return False
    if not 1920 <= int(passport['byr']) <= 2002:
        return False
    if not 2010 <= int(passport['iyr']) <= 2020:
        return False
    if not 2020 <= int(passport['eyr']) <= 2030:
        return False
    if passport['hgt'].endswith('cm'):
        if not 150 <= int(passport['hgt'].split('cm')[0]) <= 193:
            return False
    elif passport['hgt'].endswith('in'):
        if not 59 <= int(passport['hgt'].split('in')[0]) <= 76:
            return False
    else:
        return False
    if not re.match(r'^#[0-9a-f]{6}$', passport['hcl']):
        return False
    _ecls = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if passport['ecl'] not in _ecls:
        return False
    if not re.match(r'^\d{9}$', passport['pid']):
        return False
    return True


def main():
    """
    main
    """
    with open('input.txt') as fp:
        data = [line.strip() for line in fp.readlines()]

    passports = get_passports(data)

#    part1 = sum([1 for p in passports if valid_passport1(p)])
#    print('part 1 valid passports:', part1)
    part2 = sum([1 for p in passports if valid_passport2(p)])
    print('part 2 valid passports:', part2)


if __name__ == '__main__':
    main()
