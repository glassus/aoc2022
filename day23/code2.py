from collections import defaultdict

data = open('input.txt').read().splitlines()
#data = open('input_test2.txt').read().splitlines()

d = {}

for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == '#':
            d[(i,j)] = 1

def suiv(ordre):
    new = [ordre[1], ordre[2], ordre[3], ordre[0]]
    return new

ordre = ['N', 'S', 'W', 'E']

def propos(i,j, ordre):
    for dir in ordre:
        if dir == 'N':
            if (i-1,j) not in d and\
               (i-1,j-1) not in d and\
               (i-1,j+1) not in d:
                return (i-1,j)
        if dir == 'S':
            if (i+1,j) not in d and\
               (i+1,j-1) not in d and\
               (i+1,j+1) not in d:
                return (i+1,j)
        if dir == 'W':
            if (i,j-1) not in d and\
               (i-1,j-1) not in d and\
               (i+1,j-1) not in d:
                return (i,j-1)           
        if dir == 'E':
            if (i,j+1) not in d and\
               (i-1,j+1) not in d and\
               (i+1,j+1) not in d:
                return (i,j+1)
        

def isol(i,j):
    if (i-1,j) not in d and\
       (i-1,j-1) not in d and\
       (i-1,j+1) not in d and \
        (i+1,j) not in d and\
       (i+1,j-1) not in d and\
       (i+1,j+1) not in d and \
       (i, j-1) not in d and \
        (i, j+1) not in d:
            return True
    return False


def move(ordre):
    occ = defaultdict(int)
    for cpl in d:
        if isol(cpl[0], cpl[1]):
            continue
        prop = propos(cpl[0], cpl[1], ordre)
        if prop:
            occ[prop] += 1
    to_add = []
    to_rem = []
    
    for cpl in d:
        if isol(cpl[0], cpl[1]):
            continue
        prop = propos(cpl[0], cpl[1], ordre)
        if prop:
            if occ[prop] > 1:
                continue
            else:
                to_add.append(prop)
                to_rem.append(cpl)
    if to_add == []:
        return True
    for prop in to_add:
        d[prop] = 1
    for cpl in to_rem:
        del d[cpl]
    return False
        
def aff():
    for i in range(len(data)):
        s = ''
        for j in range(len(data[0])):
            if (i,j) in d:
                s += '#'
            else:
                s += '.'
        print(s)


#aff()
fini = False
i = 0
while not fini:
    i += 1
    #print('étape', i)
    fini = move(ordre)
    #aff()
    ordre = suiv(ordre)
print(i)
    
    
def rect():
    val = list(d.keys())[0]
    imin = imax = val[0]
    jmin = jmax = val[1]
    for v in d:
        imin = min(imin, v[0])
        imax = max(imax, v[0])
        jmin = min(jmin, v[1])
        jmax = max(jmax, v[1])
    emp = 0
    for i in range(imin, imax+1):
        for j in range(jmin, jmax+1):
            if (i,j) not in d:
                emp += 1
    return emp
                
#print(rect())    