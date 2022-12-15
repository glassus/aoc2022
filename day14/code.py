data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

def parse(line):
    p = []
    v = line.split(' -> ')
    for g in v:
        p.append(list(map(int, g.split(','))))
    return p

def parse_total():
    lst_paths = []
    min_x = 500
    max_x = 500
    max_y = 0
    for line in data:
        path = parse(line)
        min_x = min(min_x, min([p[0] for p in path]))
        max_x = max(max_x, max([p[0] for p in path]))
        max_y = max(max_y, max([p[1] for p in path]))
        lst_paths.append(path)
    return lst_paths, min_x, max_x, max_y

paths, min_x, max_x, max_y = parse_total()
larg = max_x - min_x + 1
haut = max_y + 1

M = [['.']*larg for _  in range(haut)]

def affiche(M):
    for line in M:
        print(''.join([v for v in line]))

def trace_paths():
    for line in paths:
        for i in range(len(line)-1):
            xmin, xmax = min(line[i][0], line[i+1][0]),\
                         max(line[i][0], line[i+1][0])
            ymin, ymax = min(line[i][1], line[i+1][1]),\
                         max(line[i][1], line[i+1][1])
            for x in range(xmin, xmax+1):
                for y in range(ymin, ymax+1):
                    M[y][x-min_x] = '#'

trace_paths()

def chute():
    n = 0
    while True:
        n += 1
        i = 0
        j = 500
        stuck = False
        while not stuck:
            #print(i)
            if i+1 > haut-1:
                return n-1
            if M[i+1][j-min_x] == '.':
                i += 1
            else:
                if M[i+1][j-min_x] in ('#', 'o'):
                    if j-min_x-1 < 0 or \
                       i+1 > haut-1 or \
                       j-min_x-1 < 0 or \
                       j-min_x+1 > larg-1 :
                        return n-1
                    
                    if M[i+1][j-min_x-1] not in ('#', 'o'):
                        i += 1
                        j -= 1
                    elif M[i+1][j-min_x+1] not in ('#', 'o'):
                        i += 1
                        j += 1
                    else:
                        M[i][j-min_x] = 'o'
                        stuck = True

print(chute())
affiche(M)

                
        
        
        
        
        
        
        
        
        
        

