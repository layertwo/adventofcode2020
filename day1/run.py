#!/usr/bin/env python3

import itertools


def main():
    """
    main
    """
    with open('input.txt') as fp:
        data = [int(line.strip()) for line in fp.readlines()]

    for outside, inside in itertools.product(data, data):
        if outside == inside:
            continue

        if outside + inside == 2020:
            print('part 1 day 1 nums:', outside, inside)
            print('part 1 day 1 answer:', outside * inside)
            break


    for outside, middle, inside in itertools.product(data, data, data):
        if outside == middle:
            continue

        if middle == inside:
            continue

        if outside + middle + inside == 2020:
            print('part 2 day 1 nums:', outside, middle, inside)
            print('part 2 day 1 answer:', outside * middle * inside)
            break


if __name__ == '__main__':
    main()
