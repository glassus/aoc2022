from collections import defaultdict

d = defaultdict(int)

data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

sep = data.index('')


for i in range(sep):
    line = data[i]
    for j in range(len(line)):
        if line[j] != ' ':
            d[(i,j)] = line[j]
            
instructions = []
raw = data[sep+1]
i = 0
while i < len(raw):
    if raw[i] in ('L', 'R'):
        instructions.append(raw[i])
        i += 1
    else:
        if i != len(raw)-1 and raw[i+1] in ('L', 'R'):
            val = int(raw[i])
            instructions.append(val)
            i += 1
        else:
            val = int(raw[i:i+2])
            instructions.append(val)
            i += 2


def moveR(mr, mc):
    if (mr, mc) == (0, 1):
        return (1, 0)
    if (mr, mc) == (1, 0):
        return (0, -1)
    if (mr, mc) == (0, -1):
        return (-1, 0)
    if (mr, mc) == (-1, 0):
        return (0, 1)

def moveL(mr, mc):
    if (mr, mc) == (0, 1):
        return (-1, 0)
    if (mr, mc) == (-1, 0):
        return (0, -1)
    if (mr, mc) == (0, -1):
        return (1, 0)
    if (mr, mc) == (1, 0):
        return (0, 1)
  
def move(r, c, mr, mc, inst):
    i = 0
    while i < inst:
        i += 1
        nr = r + mr
        nc = c + mc
        if d[(nr,nc)] == '#':
            if d[(r,c)] == 0:
                r = r + mr
                c = c + mc
                while d[(r,c)] != 0:
                    r = r + mr
                    c = c + mc
                r = r - mr
                c = c - mc
            break
        if d[(nr,nc)] == 0:
            while d[(r,c)] != 0:
                r = r - mr
                c = c - mc
            i -= 1
        else:
            r = nr
            c = nc
            d[(r,c)] = 'o'
    return r, c
        
    
    
  
  
  
def parcours():
    mr, mc = 0, 1
    r, c = 0, data[0].index('.')
    for inst in instructions:
        if inst == 'L':
            mr, mc = moveL(mr, mc)
        elif inst == 'R':
            mr, mc = moveR(mr, mc)
        else:
            r, c = move(r, c, mr, mc, inst)
#         print(inst)
#         aff()
#         print(r,c)
        
    fr = r + 1
    fc = c + 1
    if (mr, mc) == (0, 1):
        fac = 0
    if (mr, mc) == (1, 0):
        fac = 1
    if (mr, mc) == (0, -1):
        fac = 2
    if (mr, mc) == (-1, 0):
        fac = 3
    print(1000*fr + 4*fc + fac)
            
def aff():
    for r in range(12):
        s = ''
        for c in range(16):
            if d[(r,c)] == 0:
                s += ' '
            else:
                s += d[(r,c)]
        print(s)