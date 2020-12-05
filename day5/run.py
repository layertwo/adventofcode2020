#!/usr/bin/env python3
from collections import Counter


def bn_space(_input, _min=0, _max=127, left='f', right='b'):
    """
    binary search with direction
    """
    for i in _input.lower():
        _mid = (_max + _min) // 2
        if i == left:
            _max = _mid
        elif i == right:
            _min = _mid + 1
        if _min == _max:
            return _max
    return 0


def bn_search(_nums):
    """
    binary search to find missing number
    """
    _nums.sort()
    _max = len(_nums)
    _min = 0
    while _min < _max:
        _mid = _min + (_max - _min) // 2
        if _nums[_mid] > _mid:
            _max = _mid
        else:
            _min = _mid + 1
    return _min


def get_seat(_input):
    """
    get seat from input
    """
    row = bn_space(_input[:7])
    column = bn_space(_input[7:],
                      _max=7,
                      left='l',
                      right='r')
    return (row, column)


def get_seat_id(row, column):
    """
    get seat from input
    """
    return row * 8 + column


def find_my_seat(_input, _max=None):
    """
    determine row occurences
    """
    for r in [r[0] for r in Counter([s[0] for s in _input]).items() if r[1] < 8]:
        if r == _max:
            continue
        return (r, bn_search([s[1] for s in _input if s[0] == r]))


def main():
    """
    main
    """
    with open('input.txt') as fp:
        data = [line.strip() for line in fp.readlines()]

    seats = [get_seat(d) for d in data]
    max_seat = sorted(seats, reverse=True)[0]
    print(f'row {max_seat[0]}, column {max_seat[1]}, seat id {get_seat_id(*max_seat)}')

    my_seat = find_my_seat(seats, _max=max_seat[0])
    print(f'row {my_seat[0]}, column {my_seat[1]}, seat id {get_seat_id(*my_seat)}')


if __name__ == '__main__':
    main()
