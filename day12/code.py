data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()
from random import choice

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
        if ord(lettre(couple[0], couple[1])) <= ord(lettre(i,j)) + 1 :
            poss.append(couple)
    
    return poss
    
tab[start[0]][start[1]] = '`'
tab[end[0]][end[1]] = '{'

def cherche_chemin():
    global visited
    visited = []
    chemin = ''
    trace = []
    current = end

    fini = False
    while not fini:
        chemin += lettre(current[0],current[1])
        trace.append(current)
        visited.append(current)
        
        poss = possibles(current[0],current[1])
        if len(poss) == 0:
            fini = True
        else:
            if (current[0]-1, current[1]) in poss:
                current = (current[0]-1, current[1])
            else:
                current = choice(poss)

    return chemin

def trouve():
    chemin = 'j'
    while chemin[-1] != '`':
        chemin = cherche_chemin()
        #print(chemin)
    print(len(chemin), chemin)

trouve()



