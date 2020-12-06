#!/usr/bin/env python3


def part1(data):
    """
    day 2 part 1
    """
    for _range, letter, password in data:
        letter = letter.replace(':', '')
        _min, _max = _range.split('-')
        if int(_min) <= password.count(letter) <= int(_max):
            yield 1


def part2(data):
    """
    day 2 part 1
    """
    for _range, letter, password in data:
        letter = letter.replace(':', '')
        idx1, idx2 = _range.split('-')

        v1 = password[int(idx1) - 1]
        v2 = password[int(idx2) - 1]

        # if vals are equal, continue
        if v1 == v2:
            continue

        # we already know v1 != v2
        # find if letter is in either
        if letter in (v1, v2):
            yield 1


def main():
    """
    main
    """
    with open('input.txt') as fp:
        data = [line.split() for line in fp.read().splitlines()]

    print('part 1 valid passwords:', sum(part1(data)))
    print('part 2 valid passwords:', sum(part2(data)))


if __name__ == '__main__':
    main()
