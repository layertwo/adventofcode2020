#!/usr/bin/env python3
from collections import Counter


def get_groups(_input):
    """
    get groups from input
    """
    group = []
    for idx, line in enumerate(_input):
        if not line and group:
            yield group
            group = []
            continue

        group.append(list(line))

        if idx + 1 == len(_input) and group:
            yield group


def count_answers(groups):
    """
    part 2: count answers
    """
    for g in groups:
        c = Counter([l for e in g for l in e])
        yield sum(1 for k, v in c.items() if v >= len(g))


def main():
    """
    main
    """
    with open('input.txt') as fp:
        data = fp.read().splitlines()

    print('part1 sum:', sum([len({l for e in g for l in e}) for g in get_groups(data)]))
    print('part2 sum:', sum(count_answers(get_groups(data))))


if __name__ == '__main__':
    main()
