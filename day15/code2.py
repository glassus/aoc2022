import portion as P
data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

l = 'Sensor at x=2, y=18: closest beacon is at x=-2, y=15'
def parse(l):
    l = l.split(': closest beacon is at x=')
    p = l[0].split('Sensor at x=')
    q = p[1].split(', y=')
    xs, ys = list(map(int,q))[0], list(map(int,q))[1]
    q = l[1].split(', y=')
    xb, yb = list(map(int,q))[0], list(map(int,q))[1]
    return xs, ys, xb, yb


zones = [parse(l) for l in data]

def lim(y, zone):
    xs, ys, xb, yb = zone
    d = abs(xs-xb) + abs(ys-yb)
    if (y < ys - d) or (y > ys + d):
        return None
    delta = d - abs(y-ys)
    return xs-delta, xs+delta
    
def limites(y):
    l = []
    for zone in zones:
        v = lim(y, zone)
        if v is not None:
            l.append(v)
    return l

def count(y):
    couples = limites(y)
    #print(couples)
    s = set()
    for couple in couples:
        for k in range(couple[0], couple[1]+1):
            s.add(k)
    #print(s)
    return len(s)

#y = 2000000
#y = 10

def nb_to_rm(y):
    n = 0
    setx = set()
    for zone in zones:
        if zone[3] == y and zone[2] not in setx:
            n += 1
            setx.add(zone[2])
    return n

# sol = count(y) - nb_to_rm(y)
# print(sol)
# import time
# t0 = time.time()
# lst = []
# for y in range(4000000):
#     lst.append(limites(y))
# print(time.time() - t0)

#lst = [(12, 14), (6, 10), (-8, 12), (16, 26)]

first_step = lambda s: (P.OPEN, (s.lower - 1 if s.left is P.CLOSED else s.lower), (s.upper + 1 if s.right is P.CLOSED else s.upper), P.OPEN)
second_step = lambda s: (P.CLOSED, (s.lower + 1 if s.left is P.OPEN else s.lower), (s.upper - 1 if s.right is P.OPEN else s.upper), P.CLOSED)
discretize = lambda i: i.apply(first_step).apply(second_step)



def union(lst):
    s = P.closed(lst[0][0], lst[0][1])
    for i in range(1, len(lst)):
        s = discretize(s | P.closed(lst[i][0],lst[i][1]))
    return list(s)

val_max = 4*10**6

def search():
    for y in range(3380000, 2*10**6, -1):
        print(y)
        if len(union(limites(y))) > 1:
            return y, union(limites(y))
#print(search())
    
sol = (3042458, [[-894242,3012820], [3012822,4674452]])

y = 3042458
x = 3012820 + 1
print(val_max*x + y)

