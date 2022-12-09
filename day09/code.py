data = open('input.txt').read().splitlines()
data = open('input_test.txt').read().splitlines()

import numpy as np

instructions = []
for line in data:
    direction, value = line.split()[0], int(line.split()[1])
    instructions.append([direction, value])
    
xmax, ymax, xmin, ymin = 0,0,0,0
x, y = 0,0
for inst in instructions:
    if inst[0] == 'R':
        x += inst[1]
        xmax = max(x, xmax)
    if inst[0] == 'L':
        x -= inst[1]
        xmin = min(x, xmin)
    if inst[0] == 'U':
        y += inst[1]
        ymax = max(y, ymax)
    if inst[0] == 'D':
        y -= inst[1]
        ymin = min(y, xmin)
        
range_x = xmax-xmin + 2
range_y = ymax-ymin + 2
start_x = abs(xmin)
start_y = abs(ymin)

M = np.zeros((range_x, range_y))
x = start_x
y = start_y
xT, yT = x, y

def dist():
    return abs(xT-x) + abs(yT-y)

def follow():
    global xT, yT
    delta_x = x - xT
    delta_y = y - yT
    if dist() == 2:
        if delta_x == 2:
            xT += 1
        if delta_x == -2:
            xT -= 1
        if delta_y == 2:
            yT += 1
        if delta_y == -2:
            yT -= 1
    if dist() == 3:
            xT += delta_x // abs(delta_x)
            yT += delta_y // abs(delta_y)
    #print("(x,y)", x,y, "(xT,yT)", xT, yT)
    M[xT,yT] = 1
        



for inst in instructions:
    if inst[0] == 'R':
        for k in range(inst[1]):
            x += 1
            follow()
    if inst[0] == 'L':
        for k in range(inst[1]):
            x -= 1
            follow()
    if inst[0] == 'U':
        for k in range(inst[1]):
            y += 1
            follow()
    if inst[0] == 'D':
        for k in range(inst[1]):
            y -= 1
            follow()

print(np.sum(M))