path = 'input.txt'

l = []

with open(path, 'r') as file:
    for row in file:
        l.append([int(c) for c in row.strip()])


def getJoltage(row, n):
    if n > len(row):
        return 0

    result = []
    rem = len(row) - n

    for d in row:
        while rem > 0 and result and d > result[-1]:
            result.pop()
            rem -= 1

        result.append(d)

    result = result[:n]

    return int("".join([str(d) for d in result]))


def part1(list):
    """ part 1 """

    result = 0

    for row in list:
        result += getJoltage(row, 2)

    return result


def part2(list):
    """ part 2 """

    result = 0

    for row in list:
        result += getJoltage(row, 12)

    return result


print(part1(l))
print(part2(l))
