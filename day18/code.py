data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

def contact(c1, c2):
    return abs(c1[0]-c2[0]) + \
       abs(c1[1]-c2[1]) + \
       abs(c1[2]-c2[2]) == 1

cubes = []
for line in data:
    x, y, z = list(map(int,line.split(',')))
    cubes.append((x,y,z))

nb = 0
for i in range(len(cubes)):
    for j in range(i+1, len(cubes)):
        if contact(cubes[i], cubes[j]):
            nb += 1

p1 =
print(6*len(cubes)-2*nb)
            
def trapped(c):
    (x,y,z) = c
    if (x+1,y,z) not in cubes:
        return False
    if (x-1,y,z) not in cubes:
        return False
    if (x,y+1,z) not in cubes:
        return False
    if (x,y-1,z) not in cubes:
        return False
    if (x,y,z-1) not in cubes:
        return False
    if (x,y,z+1) not in cubes:
        return False
    return True

envz = {}
for c in cubes:
    (x,y,z) = c
    if (x,y) not in envz:
        zmin = zmax = z
        for cub in cubes:
            (xc,yc,zc) = cub
            if (x,y) == (xc,yc):
                zmax = max(zmax, zc)
                zmin = min(zmin, zc)
        envz[(x,y)] = (zmin,zmax)

envy = {}
for c in cubes:
    (x,y,z) = c
    if (x,z) not in envy:
        ymin = ymax = y
        for cub in cubes:
            (xc,yc,zc) = cub
            if (x,z) == (xc,zc):
                ymax = max(ymax, yc)
                ymin = min(ymin, yc)
        envy[(x,z)] = (ymin,ymax)

envx = {}
for c in cubes:
    (x,y,z) = c
    if (y,z) not in envx:
        xmin = xmax = x
        for cub in cubes:
            (xc,yc,zc) = cub
            if (y,z) == (yc,zc):
                xmax = max(xmax, xc)
                xmin = min(xmin, xc)
        envx[(y,z)] = (xmin,xmax)







videsz = set()
for cpl in envz:
    (x,y) = cpl
    (zmin, zmax) = envz[cpl]
    for z in range(zmin, zmax):
        if (x,y,z) not in cubes:
            videsz.add((x,y,z))
            
videsy = set()
for cpl in envy:
    (x,z) = cpl
    (ymin, ymax) = envy[cpl]
    for y in range(ymin, ymax):
        if (x,y,z) not in cubes:
            videsy.add((x,y,z))            
            
videsx = set()
for cpl in envx:
    (y,z) = cpl
    (xmin, xmax) = envx[cpl]
    for x in range(xmin, xmax):
        if (x,y,z) not in cubes:
            videsx.add((x,y,z))  

vides = videsx.intersection(videsy).intersection(videsz)
vides = list(vides)

nb = 0
for i in range(len(vides)):
    for j in range(i+1, len(vides)):
        if contact(vides[i], vides[j]):
            nb += 1
            
print(6*len(vides)-2*nb)
