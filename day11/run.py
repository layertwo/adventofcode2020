#!/usr/bin/env python3
from collections import Counter
import itertools


class SeatMap:
    """Seat map class."""

    def __init__(self, data):
        """Init."""
        self.data = data
        self.width = len(data[0]) - 1
        self.length = len(data) - 1

    def render(self, data=None):
        """Render data as floor map."""
        if not data:
            data = self.data
        for line in data:
            print(''.join(line))
        print()

    def run(self):
        """Run exercise."""
        output = []
        for y, row in enumerate(self.data):
            new_row = []
            for x, seat in enumerate(row):
                seats = self.adj_seats(x, y)
                occupied = seats.get('#', 0)
                if seat == 'L':
                    if occupied == 0:
                        new_row.append('#')
                    else:
                        new_row.append(seat)
                elif seat == '#':
                    if occupied >= 4:
                        new_row.append('L')
                    else:
                        new_row.append(seat)
                else:
                    new_row.append(seat)

            output.append(new_row)
        return output

    def adj_seats(self, x, y):
        """Find adjacent seats."""
        seats = []
        if y > 0:
            seats.append(self.data[y-1][x]) # up
            if x > 0:
                seats.append(self.data[y-1][x-1]) # up left
        if y < self.length:
            seats.append(self.data[y+1][x]) # down
            if x > 0:
                seats.append(self.data[y+1][x-1]) # down left
        if x > 0:
            seats.append(self.data[y][x-1]) # left
        if x < self.width:
            seats.append(self.data[y][x+1]) # right
            if y < self.length:
                seats.append(self.data[y+1][x+1]) # down right
        if y > 0 and x < self.width:
            seats.append(self.data[y-1][x+1]) # up right
        return Counter(seats)

    def occupied_seats(self):
        """Get empty seats from map."""
        c = Counter(itertools.chain(*self.data))
        return c.get('#', 0)


def main():
    """Main"""
    with open('input.txt') as fp:
        data = [[s for s in line] for line in fp.read().splitlines()]

    s = SeatMap(data)
    old = None
    while True:
        new = s.run()

        if new == old:
            s.render(new)
            print('part 1 answer:', s.occupied_seats())
            break

        s.data = new
        old = new

if __name__ == '__main__':
    main()
