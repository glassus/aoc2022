data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

from collections import defaultdict

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

d = defaultdict(int)

def affiche():
    for i in range(max_y+1):
        for j in range(min_x, max_x+1):
            v = d[(i,j)]
            if v == 0:
                print('-', end='')
            else:
                print(v, end='')
        print()
            

def trace_paths():
    for line in paths:
        for i in range(len(line)-1):
            xmin, xmax = min(line[i][0], line[i+1][0]),\
                         max(line[i][0], line[i+1][0])
            ymin, ymax = min(line[i][1], line[i+1][1]),\
                         max(line[i][1], line[i+1][1])
            for x in range(xmin, xmax+1):
                for y in range(ymin, ymax+1):
                    d[(y,x)] = '#'

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
                print('ici')
                return n-1
            if d[(i+1,j)] == 0:
                i += 1
            else:
                if d[(i+1,j)] in ('#', 'o'):
                    if j < 0 or \
                       i+1 > max_y or \
                       j+1 > max_x :
                        print('là')
                        return n-1
                    
                    if d[(i+1,j-1)] not in ('#', 'o'):
                        i += 1
                        j -= 1
                    elif d[(i+1,j+1)] not in ('#', 'o'):
                        i += 1
                        j += 1
                    else:
                        d[(i,j)] = 'o'
                        stuck = True

print('val :', chute())
#affiche()

                
        
        
        
        
        
        
        
        
        
        

