#!/usr/bin/env python3

import itertools


def count_numbers(_input, _range=25):
    """
    find if 2 prev nums in _range == num
    """
    for idx, num in enumerate(_input):
        prev_nums = _input[idx-_range:idx]
        can_add = False
        for n1, n2 in itertools.product(prev_nums, prev_nums):
            if n1 == n2:
                continue
            if n1 + n2 == num:
                #print(f'{n1} + {n2} = {num}')
                can_add = True
                break

        if not can_add and prev_nums:
            return num

    # no op
    return 0


def contiguous(_input, val):
    """
    find contiguous range that sum val
    """
    for idx1, n1 in enumerate(_input):
        #if n1 == val:
        #    print('blah')
        #    continue

        count = n1
        for idx2, n2 in enumerate(_input[idx1:]):
            if n1 == n2:
                continue
            if count == val:
                new_nums = sorted(_input[idx1:idx1+idx2+1])
                #pprint(new_nums)
                if new_nums:
                    return new_nums[0] + new_nums[-1]
            count += n2

    # no op
    return 0

def main():
    """
    main
    """
    with open('input.txt') as fp:
        data = [int(line) for line in fp.read().splitlines()]

    invalid_num = count_numbers(data)
    print(f'part 1: {invalid_num}')
    print(f'part 2: {contiguous(data, invalid_num)}')


if __name__ == '__main__':
    main()
