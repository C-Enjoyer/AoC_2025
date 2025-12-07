path = 'input.txt'

g = []
s = -1

with open(path, 'r') as file:
    for row in file:
        r = row.strip()
        if s == -1:
            for i in range(len(r)):
                if r[i] == 'S':
                    s = i

        g.append(list(r))


def part1(grid, start):

    result = 0
    beams = set()
    beams.add(start)

    for row in grid[1:]:
        for i in range(len(row)):
            if row[i] == '^' and i in beams:
                result += 1
                beams.remove(i)
                beams.add(i - 1)
                beams.add(i + 1)

    return result

    
def part2(grid, start):

    beams = [0] * len(grid[0])
    beams[start] = 1

    for row in grid[1:]:
        for i in range(len(row)):
            if row[i] == '^' and beams[i]:
                beams[i - 1] += beams[i]
                beams[i + 1] += beams[i]
                beams[i] = 0

    return sum(beams)


print(part1(g, s))
print(part2(g, s))
