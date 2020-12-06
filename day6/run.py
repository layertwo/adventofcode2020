#!/usr/bin/env python3

from collections import Counter


def get_groups(_input):
    """
    get groups from input
    """
    output = []
    group = []
    for idx, line in enumerate(_input):
        if not line and group:
            output.append(group)
            group = []
            continue

        group.append(list(line))

        if idx + 1 == len(_input):
            if group:
                output.append(group)
    return output


def count_answers(groups):
    """
    part 2: count answers
    """
    output = []
    for g in groups:
        num = len(g)
        c = Counter([l for e in g for l in e])
        output.append(sum(1 for k, v in c.items() if v >= num))
    return output


def main():
    """
    main
    """
    with open('input.txt') as fp:
        data = fp.read().splitlines()

    groups = get_groups(data)
    print('part1 sum:', sum([len({l for e in g for l in e}) for g in groups]))
    print('part2 sum:', sum(count_answers(groups)))


if __name__ == '__main__':
    main()
