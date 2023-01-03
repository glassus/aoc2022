from collections import defaultdict

data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()
instructions = data[0]

def pieces(tour, hmax):
    p = []
    #barre horizontale
    if (tour-1) % 5 == 0:
        p.append([hmax+3, 2])
        p.append([hmax+3, 3])
        p.append([hmax+3, 4])
        p.append([hmax+3, 5])
    #plus
    if (tour-1) % 5 == 1:
        p.append([hmax+4, 2])
        p.append([hmax+3, 3])
        p.append([hmax+4, 4])
        p.append([hmax+4, 3])
        p.append([hmax+5, 3])
    #L
    if (tour-1) % 5 == 2:
        p.append([hmax+3, 2])
        p.append([hmax+3, 3])
        p.append([hmax+3, 4])
        p.append([hmax+4, 4])
        p.append([hmax+5, 4])
    #barre verticale
    if (tour-1) % 5 == 3:
        p.append([hmax+3, 2])
        p.append([hmax+4, 2])
        p.append([hmax+5, 2])
        p.append([hmax+6, 2])
    #carre
    if (tour-1) % 5 == 4:
        p.append([hmax+3, 2])
        p.append([hmax+3, 3])
        p.append([hmax+4, 2])
        p.append([hmax+4, 3])
    return p

def aff(hmax):
    for i in range(hmax+6, -2, -1):
        s = ''
        for j in range(7):
            if [i,j] in map or [i,j] in nextpos:
                s += '#'
            else:
                s += '.'
        print(s)

def sol(n):
    inst = 0
    hmax = 0
    map = [[-1,k] for k in range(0,7)]

    for tour in range(1, n+1):
        nextpos = pieces(tour, hmax)
        blocked = False
        
        while not blocked:
            inst = inst % len(instructions)
            move = instructions[inst]
            if move == '>':
                for i in range(len(nextpos)):
                    nextpos[i][1] += 1
                if any([pos[1] > 6 for pos in nextpos]) or \
                   any([pos in map for pos in nextpos]):
                    for i in range(len(nextpos)):
                        nextpos[i][1] -= 1
            
            if move == '<':
                for i in range(len(nextpos)):
                    nextpos[i][1] -= 1             
                if any([pos[1] < 0 for pos in nextpos]) or \
                   any([pos in map for pos in nextpos]):
                    for i in range(len(nextpos)):
                        nextpos[i][1] += 1
                        
            inst += 1
            for i in range(len(nextpos)):
                nextpos[i][0] -= 1
            #controle blockage bas
            if any([pos in map for pos in nextpos]):
                blocked = True
                for i in range(len(nextpos)):
                    nextpos[i][0] += 1

                for pos in nextpos:
                    map.append(pos)
                    
                    
                hmax = max([pos[0] for pos in map])+1

    return hmax

def modulo(n):
    return all([sol(100+(k+2)*n)-sol(100+(k+1)*n) == sol(100+(k+1)*n)-sol(100+(k+0)*n) for k in range(4)])


# n = 1
# while not modulo(n):
#     print(n)
#     n += 1
# print(n)

print(sol(2022))




