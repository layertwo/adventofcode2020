#!/usr/bin/env python3


class Ship:
    """Ship class."""
    def __init__(self, data):
        """Init."""
        self.x = 0
        self.y = 0
        self.heading = 90
        self.data = data

    def run(self):
        """Run ship."""
        for line in self.data:
            action = line[:1]
            num = int(line[1:])

            if  action == 'N':
                self.y += num
            elif action == 'S':
                self.y -= num
            elif action == 'E':
                self.x += num
            elif action == 'W':
                self.x -= num
            elif action == 'L':
                self.heading = (self.heading - num) % 360
            elif action == 'R':
                self.heading = (self.heading + num) % 360
            elif action == 'F':
                self.heading_dir(num)

    def heading_dir(self, num):
        """Get heading to direction"""
        val = round(self.heading / 90)
        if val == 0:
            self.y += num
        elif val == 1:
            self.x += num
        elif val == 2:
            self.y -= num
        elif val == 3:
            self.x -= num

    @property
    def position(self):
        """Get current position."""
        return self.x , self.y


def manhattan_distance(x, y):
    """Manhattan distance."""
    return abs(0-x) + abs(0-y)


def main():
    """Main."""
    with open('input.txt') as fp:
        data = fp.read().splitlines()

    s = Ship(data)
    s.run()
    print('day 12 part 1:', manhattan_distance(*s.position))


if __name__ == '__main__':
    main()
