data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()
#data = open('day24.txt').read().splitlines()


haut =  len(data)
larg = len(data[0])
start = (0,1)
end = (haut-2, larg-2)

mapp = {}

t = 0
mapp[0] = {}

def init_mapp():
    for i in range(haut):
        for j in range(larg):
            mapp[0][(i,j)] = data[i][j]
init_mapp()


def make_mapp(t):
    assert t-1 in mapp
    mapp[t] = {}
    for i in range(haut):
        for j in range(larg):
            mapp[t][(i,j)] = []
    for i in range(haut):
        for j in range(larg):       
            if i == 0 or j == 0 or i == haut-1 or j == larg-1:
                mapp[t][(i,j)] = mapp[t-1][(i,j)]
            else:
                for car in mapp[t-1][(i,j)]:
                    if car == '>':
                        mapp[t][(i,j%(larg-2)+1)].append(car)
                    if car == '<':
                        mapp[t][(i,(j-2)%(larg-2)+1)].append(car)
                    if car == '^':
                        mapp[t][((i-2)%(haut-2)+1,j)].append(car)
                    if car == 'v':
                        mapp[t][(i%(haut-2)+1,j)].append(car)

def aff(t, visited=[]):
    for i in range(haut):
        s = ''
        for j in range(larg):
            if (i,j) == current:
                s += 'E'
#                 else:
#                     s += 'O'
            else:
                if mapp[t][(i,j)] == []:
                    s += '.'
                elif len(mapp[t][(i,j)]) > 1:
                    s += str(len(mapp[t][(i,j)]))
                else:
                    s += mapp[t][(i,j)][0]
        print(s)
        
def futurs_libres(t, i, j):
    vois = []
    dxy = [(-1,0),(0,-1),(1,0),(0,1)]
    for dx, dy in dxy:
        nx, ny = i+dx, j+dy
        if nx <= 0 or nx >= haut-1:
            continue
        if ny <= 0 or ny >= larg-1:
            continue
        vois.append((nx,ny))

    sol = []
    if t not in mapp:
        make_mapp(t)
    for x,y in vois:
        if mapp[t][(x,y)] == []:
            sol.append((x,y))
    if (i,j) == (haut-2, larg-2):
        sol.append(end)
    return sol


base_explo = []
stock = []

visited = {}


base_explo.append(start)


t = 0
while end not in visited:
    to_explore = []
    #print("minute", t)
    #print("bases à explorer", base_explo)
    for base in base_explo:
        #print("base actuelle", base, end = ' ')
        if base not in visited:
            visited[base] = t

        neigh = futurs_libres(t+1, base[0], base[1])
        neigh.append(base)

        for vois in neigh:
            if vois not in to_explore:
                to_explore.append(vois)
                #print("qui rajoute :", vois)
    
    
    base_explo = list(to_explore)
    #print("à explorer:", base_explo)
    #print()
    #print()
#     #aff(t, visited)
    

    #print()     
    t += 1
    
    
    
        
print('sol', visited[end]+1)  