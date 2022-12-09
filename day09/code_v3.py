data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()



instructions = []
for line in data:
    direction, value = line.split()[0], int(line.split()[1])
    instructions.append([direction, value])
    
d = {'R':(1,0),
     'L':(-1,0),
     'U':(0,1),
     'D':(0,-1)}

def add(t1,t2):
    return (t1[0]+t2[0], t1[1]+t2[1])

start_x = 0
start_y = 0

visited = set()

size = 10
snake = [[start_x, start_y] for _ in range(size)]


def dist(t1, t2):
    return abs(t1[0]-t2[0]) + abs(t1[1]-t2[1])

def follow(tH, tT):
    delta_x = tH[0] - tT[0]
    delta_y = tH[1] - tT[1]
    if dist(tH, tT) == 2:
        if delta_x == 2:
            tT = add(tT,d['R'])
        if delta_x == -2:
            tT = add(tT,d['L'])
        if delta_y == 2:
            tT = add(tT,d['U'])
        if delta_y == -2:
            tT = add(tT,d['D'])
    if dist(tH,tT) >= 3:
            tT = add(tT,(delta_x // abs(delta_x), 0))
            tT = add(tT,(0, delta_y // abs(delta_y)))

    return tT
 
 
for inst in instructions:
    for k in range(inst[1]):
        snake[0] = add(snake[0], d[inst[0]])
        for i in range(0, size-1):
            snake[i+1] = follow(snake[i], snake[i+1])
        visited.add(tuple(snake[-1]))

print(len(visited))