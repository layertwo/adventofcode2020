#!/usr/bin/env python3

class Bag:
    """
    Bag class

    based on work from wbh1
    """
    def __init__(self, color, data):
        """
        init
        """
        self.data = data
        self._bags = data[color]

    @property
    def bags(self):
        """
        get nested bags
        """
        for clr, num in iter(self._bags.items()):
            new_bags = Bag(clr, self.data).bags
            if not new_bags:
                yield self._bags
            bags = self._bags.copy()
            for val in iter(new_bags):
                for k, v in val.items():
                    if k in bags:
                        bags[k] += v * num
                    else:
                        bags[k] = v * num
            self._bags = bags
        yield self._bags

    def __len__(self):
        """
        get how many bags
        """
        return sum([v for b in self.bags for k, v in b.items()])


def process_input(_input):
    """
    process input
    """
    output = {}
    for line in _input:
        if line:
            color = line.split('bags', 1)[0].strip()
            output[color] = {}
            if not 'no other bags' in line:
                for val in line.split('contain ')[1].split(', '):
                    val = val.split()
                    output[color].update({f'{" ".join(val[1:3])}': int(val[0])})
    return output


def main():
    """
    main
    """
    with open('input.txt') as fp:
        data = process_input(fp.read().splitlines())

    num = 0
    for clr in data:
        b = Bag(clr, data)
        num += sum([1 for b in b.bags if 'shiny gold' in b])
    print(f'part 1 shiny gold bags: {num}')

    b = Bag('shiny gold', data)
    print(f'part 2 shiny gold bags: {len(b)}')


if __name__ == '__main__':
    main()
