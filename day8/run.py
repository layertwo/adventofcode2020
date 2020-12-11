#!/usr/bin/env python3

def accumulator(_input):
    """
    do action
    """
    accum = 0
    counter = set()
    status = True
    i = 0
    while i < len(_input):
        if (i, _input[i]) in counter:
            status = False
            #print('infinite loop')
            break

        act, num = _input[i].split()
        counter.add((i, _input[i]))
        if act == 'acc':
            accum += int(num)
            i += 1
        elif act == 'jmp':
            i += int(num)
        else:
            i += 1

    return accum, status


def non_infinite(_input):
    """
    find non infinite loops
    """
    _input.copy()
    for idx, line in enumerate(_input):
        new_data = _input.copy()

        action, _ = line.split()
        if action == 'jmp':
            new_data[idx] = line.replace('jmp', 'nop')
        elif action == 'nop':
            new_data[idx] = line.replace('nop', 'jmp')
        else:
            continue

        # walrus operator, anyone?
        if (result := accumulator(new_data))[1]:
            return result[1]

    return 0


def main():
    """
    main
    """
    with open('input.txt') as fp:
        data = fp.read().splitlines()

    print('part 1 accumulator:', accumulator(data)[0])
    print('part 2 boot fix:', non_infinite(data)[0])


if __name__ == '__main__':
    main()
