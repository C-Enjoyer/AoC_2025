path = 'input.txt'

l = []

with open(path, 'r') as file:
    for row in file:
        for r in row.strip().split(','):
            lo, up = r.split('-')
            l.append((int(lo), int(up)))


def part1(list):
    """ part 1 """

    def isValid(num):
        strNum = str(num)

        if len(strNum) % 2 != 0:
            return True

        h = len(strNum) // 2

        return strNum[:h] != strNum[h:]

    result = 0

    for lo, up in list:
        for n in range(lo, up + 1):
            if not isValid(n):
                result += n

    return result


def part2(list):
    """ part 2 """

    def isValid(num):
        strNum = str(num)
        strLen = len(strNum)

        for ssLen in range(1, strLen // 2 + 1):
            if strLen % ssLen != 0:
                continue
            substrings = [strNum[i * ssLen: (i + 1) * ssLen] for i in range(strLen // ssLen)]
            if all(sub == substrings[0] for sub in substrings[1:]):
                return False

        return True

    result = 0

    for lo, up in list:
        for n in range(lo, up + 1):
            if not isValid(n):
                result += n

    return result


print(part1(l))
print(part2(l))
