data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

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

size = 10
snake = [[start_x, start_y] for _ in range(size)]


def dist(xH, yH, xT, yT):
    return abs(xT-xH) + abs(yT-yH)

def follow(xH, yH, xT, yT):
    delta_x = xH - xT
    delta_y = yH - yT
    if dist(xH, yH, xT, yT) == 2:
        if delta_x == 2:
            xT += 1
        if delta_x == -2:
            xT -= 1
        if delta_y == 2:
            yT += 1
        if delta_y == -2:
            yT -= 1
    if dist(xH, yH, xT, yT) >= 3:
            xT += delta_x // abs(delta_x)
            yT += delta_y // abs(delta_y)

    return (xT, yT)
        



for inst in instructions:
    if inst[0] == 'R':
        for k in range(inst[1]):
            snake[0][0] += 1
            for i in range(0, size-1):
                snake[i+1][0], snake[i+1][1] = follow(snake[i][0], snake[i][1], snake[i+1][0], snake[i+1][1])
            M[snake[-1][0], snake[-1][1]] = 1
            
    if inst[0] == 'L':
        for k in range(inst[1]):
            snake[0][0] -= 1
            for i in range(0, size-1):
                snake[i+1][0], snake[i+1][1] = follow(snake[i][0], snake[i][1], snake[i+1][0], snake[i+1][1])
            M[snake[-1][0], snake[-1][1]] = 1
            
    if inst[0] == 'U':
        for k in range(inst[1]):
            snake[0][1] += 1
            for i in range(0, size-1):
                snake[i+1][0], snake[i+1][1] = follow(snake[i][0], snake[i][1], snake[i+1][0], snake[i+1][1])
            M[snake[-1][0], snake[-1][1]] = 1
            
    if inst[0] == 'D':
        for k in range(inst[1]):
            snake[0][1] -= 1
            for i in range(0, size-1):
                snake[i+1][0], snake[i+1][1] = follow(snake[i][0], snake[i][1], snake[i+1][0], snake[i+1][1])
            M[snake[-1][0], snake[-1][1]] = 1
    #print(snake)
    

print(np.sum(M))