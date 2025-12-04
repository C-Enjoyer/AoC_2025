path = 'input.txt'

g = []

with open(path, 'r') as file:
    for row in file:
        g.append(list(row.strip()))


def getGrid(grid, r, c):
    if not (0 <= r < len(grid)) or not (0 <= c < len(grid[0])):
        return '.'
    return grid[r][c]


def surMax(grid, r, c, m):
    cnt = 0
    for rs in [-1, 0, 1]:
        for cs in [-1, 0, 1]:
            if rs == 0 and cs == 0:
                continue
            if getGrid(grid, r + rs, c + cs) == '@':
                cnt += 1
                if cnt >= m:
                    return False

    return True


def getRemovable(grid):

    removable = []

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != '@':
                continue

            if surMax(grid, r, c, 4):
                removable.append((r, c))

    return removable


def part1(grid):
    """ part 1 """

    return len(getRemovable(grid))


def part2(grid):
    """ part 2 """

    result = 0
    removable = getRemovable(grid)

    while removable:

        for r, c in removable:
            grid[r][c] = '.'
            result += 1

        removable = getRemovable(grid)

    return result


print(part1(g))
print(part2(g))
