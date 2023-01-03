import matplotlib.pyplot as plt
import numpy as np

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


print(6*len(cubes)-2*nb)
x_min = 10
x_max = 0
y_min = 10
y_max = 0
z_min = 10
z_max = 0 
for c in cubes:
    (x,y,z) = c
    x_min = min(x_min, x)
    y_min = min(y_min, y)
    z_min = min(z_min, z)
    x_max = max(x_max, x)
    y_max = max(y_max, y)
    z_max = max(z_max, z)    
 

envz = {}
for x in range(x_min, x_max+1):
    for y in range(y_min, y_max+1):
        if (x,y) not in envz:
            zmin = 20
            zmax = 0
            for cub in cubes:
                (xc,yc,zc) = cub
                if (x,y) == (xc,yc):
                    zmax = max(zmax, zc)
                    zmin = min(zmin, zc)
            envz[(x,y)] = (zmin,zmax)

envy = {}
for x in range(x_min, x_max+1):
    for z in range(z_min, z_max+1):
        if (x,z) not in envy:
            ymin = 20
            ymax = 0
            for cub in cubes:
                (xc,yc,zc) = cub
                if (x,z) == (xc,zc):
                    ymax = max(ymax, yc)
                    ymin = min(ymin, yc)
            envy[(x,z)] = (ymin,ymax)

envx = {}
for y in range(y_min, y_max+1):
    for z in range(z_min, z_max+1):
        if (y,z) not in envx:
            xmin = 20
            xmax = 0
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
    for z in range(zmin, zmax+1):
        if (x,y,z) not in cubes:
            videsz.add((x,y,z))
            
videsy = set()
for cpl in envy:
    (x,z) = cpl
    (ymin, ymax) = envy[cpl]
    for y in range(ymin, ymax+1):
        if (x,y,z) not in cubes:
            videsy.add((x,y,z))            
            
videsx = set()
for cpl in envx:
    (y,z) = cpl
    (xmin, xmax) = envx[cpl]
    for x in range(xmin, xmax+1):
        if (x,y,z) not in cubes:
            videsx.add((x,y,z))  

vides = videsx.intersection(videsy).intersection(videsz)
vides = list(vides)

def bons_voisins(c):
    return c in cubes or c in vides

def vrais_vides():
    vrais = []
    faux = []
    for c in vides:
        (x,y,z) = c
        if bons_voisins((x+1,y,z)) and \
               bons_voisins((x-1,y,z)) and \
               bons_voisins((x,y+1,z)) and \
               bons_voisins((x,y-1,z)) and \
               bons_voisins((x,y,z+1)) and \
               bons_voisins((x,y,z-1)):
            vrais.append(c)
        else:
            faux.append(c)
    return vrais

vides = vrais_vides()
nb = 0
for i in range(len(vides)):
    for j in range(i+1, len(vides)):
        if contact(vides[i], vides[j]):
            nb += 1
            
print(6*len(vides)-2*nb)


x, y, z = np.indices((20, 20, 20))


# def drawcube(xc, yc, zc):
#     c = (xc == x)  & \
#         (yc == y)  & \
#         (zc == z)
#     return c
# 
# 
# ax = plt.figure().add_subplot(projection='3d')
# 
# for c in cubes:
#     dess = drawcube(c[0], c[1], c[2])
#     ax.voxels(dess, facecolors='red', edgecolor='k')
# for c in vides:
#     dess = drawcube(c[0], c[1], c[2])
#     ax.voxels(dess, facecolors='blue', edgecolor='k')
# 
# plt.show()