data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()


haut =  len(data)
larg = len(data[0])

mapp = {}


def init_mapp():
    for i in range(haut):
        for j in range(larg):
            mapp[(i,j)] = data[i][j]
init_mapp()


def next_mapp(mapp):
    future = {}
    for i in range(haut):
        for j in range(larg):
            future[(i,j)] = []
    for i in range(haut):
        for j in range(larg):       
            if i == 0 or j == 0 or i == haut-1 or j == larg-1:
                future[(i,j)] = mapp[(i,j)]
            else:
                for car in mapp[(i,j)]:
                    if car == '>':
                        future[(i,j%(larg-2)+1)].append(car)
                    if car == '<':
                        future[(i,(j-2)%(larg-2)+1)].append(car)
                    if car == '^':
                        future[((i-2)%(haut-2)+1,j)].append(car)
                    if car == 'v':
                        future[(i%(haut-2)+1,j)].append(car)
    return future

def aff(trace=False, visited=[]):

    for i in range(haut):
        s = ''
        for j in range(larg):
            if trace and (i,j) in visited:
                s += 'E'
            else:
                if mapp[(i,j)] == []:
                    s += '.'
                elif len(mapp[(i,j)]) > 1:
                    s += str(len(mapp[(i,j)]))
                else:
                    s += mapp[(i,j)][0]
        print(s)
    print()


def futurs_libres(i, j):
    vois = []
    dxy = [(-1,0),(0,-1),(1,0),(0,1),(0,0)]
    for dx, dy in dxy:
        nx, ny = i+dx, j+dy
        if nx <= 0 or nx >= haut-1:
            continue
        if ny <= 0 or ny >= larg-1:
            continue
        vois.append((nx, ny))

    sol = []

    for x,y in vois:
        if mapp[(x,y)] == []:
            sol.append((x,y))
    if (x, y) == (1, 1):
        sol.append((0,1))
    if (x, y) == (haut-2, larg-2):
        sol.append((haut-1, larg-2))
    
    return sol



to_explore = []
stock = []

start = (0,1)
end = (haut-1, larg-2)


current = start
visited = {}

to_explore.append(current)


t = 0
while end not in visited:
    t += 1
    mapp = next_mapp(mapp)
    next_to_explore = []
    
    while to_explore != []:
        current = to_explore.pop()
        
        if current not in visited:
            visited[current] = t
        
        dispos = futurs_libres(current[0], current[1])
        
        for voisin in dispos:
            if voisin not in next_to_explore:
                next_to_explore.append(voisin)
                
    to_explore = next_to_explore



to_explore = []
stock = []

end = (0,1)
start = (haut-1, larg-2)


current = start
visited = {}

to_explore.append(current)



while end not in visited:
    t += 1
    mapp = next_mapp(mapp)
    next_to_explore = []
    
    while to_explore != []:
        current = to_explore.pop(0)
        
        if current not in visited:
            visited[current] = t
        
        dispos = futurs_libres(current[0], current[1])
        
        for voisin in dispos:
            if voisin not in next_to_explore:
                next_to_explore.append(voisin)
                
    to_explore = next_to_explore.copy() 
 

to_explore = []
stock = []

start = (0,1)
end = (haut-1, larg-2)


current = start
visited = {}

to_explore.append(current)



while end not in visited:
    t += 1
    mapp = next_mapp(mapp)
    next_to_explore = []
    
    while to_explore != []:
        current = to_explore.pop(0)
        
        if current not in visited:
            visited[current] = t
        
        dispos = futurs_libres(current[0], current[1])
        
        for voisin in dispos:
            if voisin not in next_to_explore:
                next_to_explore.append(voisin)
                
    to_explore = next_to_explore.copy() 
 
print(t)


