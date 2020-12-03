#!/usr/bin/env python3

import functools
import math


class Sled:
    """
    Generic Sled class
    """

    def __init__(self, filepath):
        """
        init
        """
        with open(filepath) as fp:
            self.data = [line.strip() for line in fp.readlines()]
        self.width = len(self.data[0])

    @functools.lru_cache()
    def new_position(self, placement, x, y):
        """
        calc new position
        """
        _x = (placement[0] + x) % self.width
        _y = (placement[0] + y) % self.width

        return (_x, _y)

    def find_trees(self, x, y):
        """
        find the trees in the way based on slope
        """
        placement = (0, 0)
        trees = 0
        for idx in range(0, len(self.data), abs(y)):
            if self.data[idx][placement[0]] == '#':
                trees += 1
            placement = self.new_position(placement, x, y)
        return trees

def main():
    """
    main
    """
    sl = Sled('input.txt')

    print('part1 num trees:', sl.find_trees(3, -1))

    trees = [sl.find_trees(1, -1),
             sl.find_trees(3, -1),
             sl.find_trees(5, -1),
             sl.find_trees(7, -1),
             sl.find_trees(1, -2)]

    print('part2 num trees:', math.prod(trees))


if __name__ == '__main__':
    main()
