#!/usr/bin/env python3


def part1(_input):
    """
    part 1
    """
    dif1 = 0
    dif3 = 0
    for idx, num in enumerate(_input):
        try:
            nxt = abs(_input[idx+1] - num)
            if nxt == 1:
                dif1 += 1
            if nxt == 3:
                dif3 += 1
        except IndexError:
            break

    # my adapter
    dif3 += 1

    return dif1 * dif3


def main():
    """
    main
    """
    with open('input.txt') as fp:
        data = sorted([int(line.strip()) for line in fp.readlines()])
    data.insert(0, 0)

    print('part 1 answer:', part1(data))

if __name__ == '__main__':
    main()
