import math

path = 'input.txt'

l = []
o = []

with open(path, 'r') as file:
    opis = []
    ops = ['*', '+']
    for row in file.readlines()[::-1]:
        r = row.replace('\n', '').replace('\r', '')

        if r[0] in ops:
            for i in range(len(r)):
                if r[i] in ops:
                    o.append(r[i])
                    opis.append(i)
            opis.append(len(r) + 1)

        else:
            for i, (s, e) in enumerate(zip(opis, opis[1:])):
                if len(l) <= i:
                    l.append([])
                l[i].append(r[s:e - 1])

    l = [list(reversed(sl)) for sl in l]
    

def part1(list, ops):
    """ part 1 """

    result = 0

    for i in range(len(ops)):
        if ops[i] == '+':
            result += sum([int(num) for num in list[i]])
        elif ops[i] == '*':
            result += math.prod([int(num) for num in list[i]])

    return result

    
def part2(list, ops):
    """ part 2 """

    result = 0

    for i in range(len(ops)):

        tl = []
        n = len(list[i][0])
        
        for j in range(n - 1, -1, -1):
            numStr = ""
            for k in range(len(list[i])):
                numStr += list[i][k][j]
            tl.append(int(numStr))

        if ops[i] == '+':
            result += sum(tl)
        elif ops[i] == '*':
            result += math.prod(tl)

    return result


print(part1(l, o))
print(part2(l, o))
