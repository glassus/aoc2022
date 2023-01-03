data = open('input.txt').read().splitlines()
data = open('input_test.txt').read().splitlines()

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
#mapp[(0,2,2)] = '^'

def next_mapp(t):
    mapp[t+1] = {}
    for i in range(haut):
        for j in range(larg):
            mapp[t+1][(i,j)] = []
    for i in range(haut):
        for j in range(larg):       
            if i == 0 or j == 0 or i == haut-1 or j == larg-1:
                mapp[t+1][(i,j)] = mapp[t][(i,j)]
            else:
                for car in mapp[t][(i,j)]:
                    if car == '>':
                        mapp[t+1][(i,j%(larg-2)+1)].append(car)
                    if car == '<':
                        mapp[t+1][(i,(j-2)%(larg-2)+1)].append(car)
                    if car == '^':
                        mapp[t+1][((i-2)%(haut-2)+1,j)].append(car)
                    if car == 'v':
                        mapp[t+1][(i%(haut-2)+1,j)].append(car)


def mapp_instant(t):
    init_mapp()
    for k in range(t):
        next_mapp(k)
    


def aff(t, visited):
    for i in range(haut):
        s = ''
        for j in range(larg):
            if (i,j) in visited:
                s += 'O'
            else:
                if mapp[t][(i,j)] == []:
                    s += '.'
                elif len(mapp[t][(i,j)]) > 1:
                    s += str(len(mapp[t][(i,j)]))
                else:
                    s += mapp[t][(i,j)][0]
            
                
                
        print(s)

def voisins(t,i,j):
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
    for x,y in vois:
        if mapp[t][(x,y)] == []:
            sol.append((x,y))
    if (i,j) == (haut-2, larg-2):
        sol.append(end)
    return sol

taille = 40
mapp_instant(taille)
print("maps générées")
frontier = []
current = start
visited = {}

t = 0
frontier.append((t, current))


while t < taille and end not in visited:

    if frontier != []:
        to_keep = []
        for t, pos in frontier:
            to_keep.append(t)
        to_rm = []
        for t in mapp:
            if t not in to_keep:
                to_rm.append(t)
        for t in to_rm:
            del mapp[t]
        
        current = None
        for t, pos in frontier:
            if pos not in visited:
                current = pos
                frontier.remove((t, pos))
                break
        if current is None:
            t, current = frontier.pop(0)
        
    if current not in visited:
        visited[current] = t
    next_mapp(t)
    t += 1
    vois = voisins(t, current[0], current[1])

    for neigh in vois:
        to_add = True
        for _, pos in frontier:
            if neigh == pos:
                to_add = False
        if to_add:
            frontier.append((t+1, neigh))
    #print(t, current, vois, frontier)
  
print(len(visited))
print(visited[end])
#mapp[(166,25,20)] = 'O'
#aff(166)
    