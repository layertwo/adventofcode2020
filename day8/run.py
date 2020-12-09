#!/usr/bin/env python3


def accumulator(_input):
    """
    do action
    """
    accum = 0
    counter = set()
    i = 0
    while i < len(_input):
        if (i, _input[i]) in counter:
            print('infinite loop')
            break
        act, num = _input[i]
        if act == 'acc':
            accum += int(num)
        elif act == 'jmp':
            i += int(num)
            continue
        counter.add((i, _input[i]))
        i += 1

    return accum


def get_actions(data):
    """
    get actions from file
    """
    return [tuple(line.split(' ', 1)) for line in data]


def main():
    """
    main
    """
    with open('input.txt') as fp:
        data = get_actions(fp.read().splitlines())

    print('accumulator', accumulator(data))


if __name__ == '__main__':
    main()
