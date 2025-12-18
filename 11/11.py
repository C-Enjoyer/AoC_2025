from functools import cache

path = 'input.txt'

d = {}

with open(path, 'r') as file:
    for row in file:
        index = ""

        for p in row.strip().split(' '):
            if index == "":
                index = p.replace(':', '')
                d[index] = []
            else:
                d[index].append(p)


@cache
def getPaths(start, end):
    if start == end:
        return 1

    return sum([getPaths(p, end) for p in d.get(start, [])])


def part1():
    """ part 1 """

    return getPaths("you", "out")


def part2():
    """ part 2 """

    a = getPaths("svr", "fft") * getPaths("fft", "dac") * getPaths("dac", "out")
    b = getPaths("svr", "dac") * getPaths("dac", "fft") * getPaths("fft", "out")

    return a + b


print(part1())
print(part2())
