data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()


haut =  len(data)
larg = len(data[0])

mapp = {}

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
    print(t)
    for i in range(haut):
        s = ''
        for j in range(larg):
            if (i,j) == current:
                s += 'E'
            else:
                if mapp[t][(i,j)] == []:
                    s += '.'
                elif len(mapp[t][(i,j)]) > 1:
                    s += str(len(mapp[t][(i,j)]))
                else:
                    s += mapp[t][(i,j)][0]
        print(s)
    print()
        
def futurs_libres(t, i, j):
    vois = []
    dxy = [(-1,0),(0,-1),(1,0),(0,1),(0,0)]
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
    return sol


to_explore = []
stock = []



t_start = 516
t = t_start

start = (0,1)
end = (haut-2, larg-2)

# start = (haut-1, larg-2)
# end = (1,1)


current = start
visited = {}

for t in range(1,t_start+1):
    make_mapp(t)

to_explore.append((t, current))
stock.append(current)


while end not in visited:

    t, current = to_explore.pop(0)
    stock.pop(0)
    #aff(t, visited)

    if current not in visited:
        visited[current] = t
    
    dispos = futurs_libres(t+1, current[0], current[1])
    while dispos == []:
        t += 1
        dispos = futurs_libres(t+1, current[0], current[1])
        
    for voisin in dispos:
        if voisin not in stock:
            to_explore.append((t+1, voisin))
            stock.append(voisin)
 
        
print('sol', visited[end]+1)  