data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

pairs = []
for s in data:
    s = s.split(',')
    l1 = list(map(int, s[0].split('-')))
    l2 = list(map(int, s[1].split('-')))
    pairs.append((l1, l2))
    

def contain(ia, ib):
    if ia[0] <= ib[0] and ib[1] <= ia[1]:
        return True
    if ib[0] <= ia[0] and ia[1] <= ib[1]:
        return True
    return False

#part1
print(sum([contain(p[0], p[1]) for p in pairs]))

def overlap(ia, ib):
    if ia[1] < ib[0] or ib[1] < ia[0]:
        return False
    return True

#part2
print(sum([overlap(p[0], p[1]) for p in pairs]))
 