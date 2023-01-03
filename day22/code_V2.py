from collections import defaultdict

d = defaultdict(int)

data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

sep = data.index('')
size = sep // 4

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

def BtoC(nr, nc, mr, mc):
    nr = 50 + nc - 100
    nc = 99
    if d[(nr,nc)] != '#':
        mr, mc = 0, -1
    return (nr, nc, mr, mc)

def CtoB(nr, nc, mr, mc):
    nc = 100 + nr - 50
    nr = 49
    if d[(nr,nc)] != '#':
        mr, mc = -1, 0
    return (nr, nc, mr, mc)


def BtoE(nr, nc, mr, mc):
    nr = 49-nr+100
    nc = 99
    if d[(nr,nc)] != '#':
        mr, mc = 0, -1
    return (nr, nc, mr, mc)

def EtoB(nr, nc, mr, mc):
    nr = 49-(nr-100)
    nc = 149
    if d[(nr,nc)] != '#':
        mr, mc = 0, -1
    return (nr, nc, mr, mc)


def CtoD(nr, nc, mr, mc):
    nc = nr-50+0
    nr = 100
    if d[(nr,nc)] != '#':
        mr, mc = 1, 0
    return (nr, nc, mr, mc)

def DtoC(nr, nc, mr, mc):
    nr = nc - 0 + 50
    nc = 50
    if d[(nr,nc)] != '#':
        mr, mc = 0, 1
    return (nr, nc, mr, mc)

def AtoD(nr, nc, mr, mc):
    nr = 100+ (49- nr)
    nc = 0
    if d[(nr,nc)] != '#':
        mr, mc = 0,1
    return (nr, nc, mr, mc)

def DtoA(nr, nc, mr, mc):
    nr = 0+149-nr
    nc = 50
    if d[(nr,nc)] != '#':
        mr, mc = 0,1
    return (nr, nc, mr, mc)

def AtoF(nr, nc, mr, mc):
    nr = nc-50+150
    nc = 0
    if d[(nr,nc)] != '#':
        mr, mc = 0,1
    return (nr, nc, mr, mc)

def FtoA(nr, nc, mr, mc):
    nc = 50+nr-150
    nr = 0
    if d[(nr,nc)] != '#':
        mr, mc = 1,0
    return (nr, nc, mr, mc)

def BtoF(nr, nc, mr, mc):
    nc = nc-100+0
    nr = 199
    if d[(nr,nc)] != '#':
        mr, mc = -1,0
    return (nr, nc, mr, mc)

def FtoB(nr, nc, mr, mc):
    nc = 100+nc
    nr = 0
    if d[(nr,nc)] != '#':
        mr, mc = 1,0
    return (nr, nc, mr, mc)


def EtoF(nr, nc, mr, mc):
    nr = 150+nc-50
    nc = 49
    if d[(nr,nc)] != '#':
        mr, mc = 0,-1
    return (nr, nc, mr, mc)

def FtoE(nr, nc, mr, mc):
    nc = 50+nr-150
    nr = 149
    if d[(nr,nc)] != '#':
        mr, mc = -1,0
    return (nr, nc, mr, mc)

def move(r, c, mr, mc, inst):
    i = 0
    while i < inst:
        i += 1
        nr = r + mr
        nc = c + mc

        
        if d[(nr,nc)] == 0:
            # B-C
            if 50 <= nr <= 99 and 100 <= nc <= 149:
                if (mr, mc) == (1,0):
                    nr, nc, mr, mc = BtoC(nr, nc, mr, mc)
                else:
                    nr, nc, mr, mc = CtoB(nr, nc, mr, mc)
            # B-E
            if 0 <= nr <= 49 and 150 <= nc <= 199:
                if (mr, mc) == (0,1):
                    nr, nc, mr, mc = BtoE(nr, nc, mr, mc)
            if 100 <= nr <= 149 and 100 <= nc <= 149:
                if (mr, mc) == (0,1):
                    nr, nc, mr, mc = EtoB(nr, nc, mr, mc)
 
            # C-D
            if 50 <= nr <= 99 and 0 <= nc <= 49:
                if (mr, mc) == (0,-1):
                    nr, nc, mr, mc = CtoD(nr, nc, mr, mc)
                else:
                    nr, nc, mr, mc = DtoC(nr, nc, mr, mc)
                    
            #A-D
            if 0 <= nr <= 49 and 0 <= nc <= 49:
                if (mr, mc) == (0,-1):
                    nr, nc, mr, mc = AtoD(nr, nc, mr, mc)
            if 100 <= nr <= 149 and nc < 0:
                if (mr, mc) == (0,-1):
                    nr, nc, mr, mc = DtoA(nr, nc, mr, mc)

            #A-F
            if  nr < 0 and 50 <= nc <= 99:
                if (mr, mc) == (-1,0):
                    nr, nc, mr, mc = AtoF(nr, nc, mr, mc)
            if  150 <= nr < 199 and  nc < 0:
                if (mr, mc) == (0,-1):
                    nr, nc, mr, mc = FtoA(nr, nc, mr, mc)

            #B-F
            if  nr < 0 and 100 <= nc <= 149:
                if (mr, mc) == (-1,0):
                    nr, nc, mr, mc = BtoF(nr, nc, mr, mc)
            if  nr > 199 and 0 <= nc <= 49:
                if (mr, mc) == (1,0):
                    nr, nc, mr, mc = FtoB(nr, nc, mr, mc)

            #E-F
            if  150 <= nr <= 199 and 50 <= nc <= 99:
                if (mr, mc) == (1,0):
                    nr, nc, mr, mc = EtoF(nr, nc, mr, mc)
                if (mr, mc) == (0,1):
                    nr, nc, mr, mc = FtoE(nr, nc, mr, mc)




        if d[(nr,nc)] == '#':
            break
        r = nr
        c = nc
        d[(r,c)] = 'o'
    
    return r, c, mr, mc
        
    
    
  
  
  
def parcours():
    mr, mc = 0, 1
    r, c = 0, data[0].index('.')
    #r, c = 197, 47
    #instructions = [5, 'L', 2] 
    for inst in instructions:
        if inst == 'L':
            mr, mc = moveL(mr, mc)
        elif inst == 'R':
            mr, mc = moveR(mr, mc)
        else:
            r, c, mr, mc = move(r, c, mr, mc, inst)
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
            
def aff(rmin, rmax, cmin, cmax):
    for r in range(rmin, rmax):
        s = ''
        for c in range(cmin, cmax):
            if d[(r,c)] == 0:
                s += ' '
            else:
                s += d[(r,c)]
        print(s)
        
parcours()
aff(0, 200, 0, 150)