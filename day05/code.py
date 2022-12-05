data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

from classe_pile import *

pile = [Pile() for _ in range(10)]

def parse_piles(l):
    for k in range(1,10):
        i = 1 + 4*(k-1)
        if l[i] != ' ':
            pile[k].empile(l[i])

for k in range(7,-1,-1):
    parse_piles(data[k])
    
def parse_move(t):
    t = t.split(' from ')
    nb = int(t[0].split('move ')[1])
    t = t[1].split(' to ')
    dep, arr = int(t[0]), int(t[1])
    return nb, dep, arr
    
def traite_part1(l):
    nb, dep, arr = parse_move(l)
    for _ in range(nb):
        elt = pile[dep].depile()
        pile[arr].empile(elt)

def traite_part2(l):
    nb, dep, arr = parse_move(l)
    stock = []
    for _ in range(nb):
        elt = pile[dep].depile()
        stock.append(elt)
    stock.reverse()
    for elt in stock:
        pile[arr].empile(elt)


for l in data:
    if l == '' or l[0] != 'm':
        continue
    #traite_part1(l)
    traite_part2(l)

    
sol = ''.join([p.sommet() for p in pile])
print(sol)