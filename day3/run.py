#!/usr/bin/env python3

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
            self.data = fp.read().splitlines()
        self.width = len(self.data[0])
        self.x = 0
        self.y = 0
        self.placement = (0, 0)

    def _new_position(self):
        """
        calc new position
        """
        _x = (self.placement[0] + self.x) % self.width
        _y = (self.placement[0] + self.y) % self.width
        self.placement = (_x, _y)

    def find_trees(self, x, y):
        """
        find the trees in the way based on slope
        """
        self.x = x
        self.y = y
        self.placement = (0, 0)
        trees = 0
        for idx in range(0, len(self.data), abs(y)):
            if self.data[idx][self.placement[0]] == '#':
                trees += 1
            self._new_position()
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
