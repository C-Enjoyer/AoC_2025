path = 'input.txt'

l = []

with open(path, 'r') as file:
    for row in file:
        d = row[0]
        num = int(row.strip()[1:])
        l.append((d, num))

def part1(list):
    """ part 1 """
    dial = 50
    result = 0

    for d, num in list:
        if d == 'L':
            dial -= num
        elif d == 'R':
            dial += num

        dial %= 100
        if dial == 0:
            result += 1

    return result
    
def part2(list):
    """ part 2 """
    dial = 50
    result = 0

    for d, num in list:
        to0 = 0

        if d == 'L':
            to0 = dial
            dial -= num
        elif d == 'R':
            to0 = 100 - dial
            dial += num

        if to0 == 0:
            to0 = 100

        if num >= to0:
            result += 1 + (num - to0) // 100

        dial %= 100

    return result

print(part1(l))
print(part2(l))
