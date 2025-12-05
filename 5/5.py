path = 'input.txt'

r = []
l = []

with open(path, 'r') as file:
    emptyFound = False
    for row in file:
        rs = row.strip()
        if len(rs) == 0:
            emptyFound = True
            continue

        if emptyFound:
            l.append(int(rs))
        else:
            lo, up = rs.split('-')
            r.append((int(lo), int(up)))


def part1(ranges, list):
    """ part 1 """

    result = 0

    for num in list:
        for s, e in ranges:
            if s <= num <= e:
                result += 1
                break

    return result


def part2(ranges):
    """ part 2 """

    ranges.sort(key=lambda x: x[0])
    resRanges = [ranges[0]]

    for s, e in ranges[1:]:
        ls, le = resRanges[-1]

        if s <= le + 1:
            resRanges[-1] = (ls, max(le, e))

        else:
            resRanges.append((s, e))

    result = 0

    for s, e in resRanges:
        result += e - s + 1

    return result


print(part1(r, l))
print(part2(r))
