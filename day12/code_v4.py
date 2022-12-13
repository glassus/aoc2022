data = open('input.txt').read().splitlines()
#data = open('inputB.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()
from collections import defaultdict

tab = [list(line) for line in data]


for i in range(len(tab)):
    if 'E' in tab[i]:
        linE = i
    if 'S' in tab[i]:
        linS = i
for j in range(len(tab[0])):
    if tab[linE][j] == 'E':
        colE = j
    if tab[linS][j] == 'S':
        colS = j
        
end = (linE, colE)
start = (linS, colS)

d = {}

def affiche():
    for i in range(len(tab)):
        s = ''
        for j in range(len(tab[0])):
            if d[(i,j)] != dmax:
                s += "#"
            else:
                s += tab[i][j]
        print(s)


def lettre(i,j):
    return tab[i][j]

def possibles(i,j):
    voisins = [(i-1,j), (i,j-1), (i,j+1), (i+1,j)]
    if i == 0:
        voisins = [(i,j-1), (i,j+1), (i+1,j)]
    if i == len(tab)-1:
        voisins = [(i-1,j),(i,j-1), (i,j+1)]
    if j == 0:
        voisins = [(i-1,j), (i,j+1), (i+1,j)]
    if j == len(tab[0])-1:
        voisins = [(i-1,j), (i,j-1), (i+1,j)]
    if (i,j) == (0,0):
        voisins = [(i,j+1), (i+1,j)]
    if (i,j) == (len(tab)-1,0):
        voisins = [(i-1,j), (i,j+1)]
    if (i,j) == (len(tab)-1, len(tab[0])-1):
        voisins = [(i-1,j), (i,j-1)]
    if (i,j) == (0, len(tab[0])-1):
        voisins = [(i,j-1), (i+1,j)]

    poss = []
    for couple in voisins:
        if ord(lettre(couple[0], couple[1])) <= ord(lettre(i,j)) + 1:
            poss.append(couple)
    
    return poss

dmax = 10**12
tab[start[0]][start[1]] = '`'
tab[end[0]][end[1]] = '{'

#start = (19,3)
def calc(start):
    print(start, ':', end = ' ')
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            d[(i,j)] = dmax
    d[start] = 0
    pile = [start]

    while d[end] == dmax:
        to_add = set()
        while pile != []:
            pos = pile.pop()
            for voisin in possibles(pos[0], pos[1]):
                if d[voisin] > d[pos] + 1:
                    d[voisin] = d[pos] + 1
                    to_add.add(voisin)
        if len(to_add) == 0:
            print(1000)
            return 1000
        for new in to_add:
            pile.append(new)

    print(d[end])
    return d[end]

#calc((19,3))

sol = []
for j in range(len(tab[0])):
    for i in range(len(tab)):
        if tab[i][j] == 'a':
            sol.append(calc((i,j)))
print(min(sol))

#affiche()

