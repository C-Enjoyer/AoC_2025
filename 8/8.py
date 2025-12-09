import math

path = 'input.txt'

l = []

with open(path, 'r') as file:
    for row in file:
        x, y, z = row.strip().split(',')
        l.append((int(x), int(y), int(z)))


def getDistance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)


def getIndex(setArray, num):

    for i, s in enumerate(setArray):
        if num in s:
            return i

    return -1


def connect(circuits, i1, i2):

    c1i = getIndex(circuits, i1)
    c2i = getIndex(circuits, i2)

    if c1i == -1 and c2i == -1:
        circuits.append({i1, i2})
    elif c1i == -1:
        circuits[c2i].add(i1)
    elif c2i == -1:
        circuits[c1i].add(i2)
    elif c1i != c2i:
        circuits[c1i] |= circuits[c2i]
        circuits.pop(c2i)
    else:
        return False

    return True


def part1(list, distances):
    """ part 1 """

    circuits = []

    for i in range(min(len(distances), 1000)):
        connect(circuits, distances[i][0], distances[i][1])

    circuits = sorted(circuits, key=lambda s: len(s), reverse=True)

    result = 1

    for i in range(min(len(circuits), 3)):
        result *= len(circuits[i])

    return result


def part2(list, distances):
    """ part 2 """

    circuits = []
    wires = 0
    result = -1

    for i in range(len(distances)):

        wires += 1 if connect(circuits, distances[i][0], distances[i][1]) else 0

        if wires + 1 >= len(list):
            result = list[distances[i][0]][0] * list[distances[i][1]][0]
            break

    return result


d = []

for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        d.append([i, j, getDistance(l[i], l[j])])

d = sorted(d, key=lambda s: s[2])

print(part1(l, d))
print(part2(l, d))
