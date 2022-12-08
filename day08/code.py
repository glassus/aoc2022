data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

M = [list(line) for line in data]
M = [[int(k) for k in line] for line in M]

nb = len(M)

def is_visible(i,j):
    val = M[i][j]
    if i in (0, nb-1) or j in (0, nb-1):
        return True
    if all([M[i][y] < val for y in range(j)]):
        return True
    if all([M[i][y] < val for y in range(j+1, nb)]):
        return True
    if all([M[x][j] < val for x in range(i)]):
        return True
    if all([M[x][j] < val for x in range(i+1, nb)]):
        return True
    return False

#part1
#print(sum([sum([is_visible(i,j) for i in range(nb)]) for j in range(nb)]))

def view(i,j):
    if i in (0, nb-1) or j in (0, nb-1):
        return 0
    
    val = M[i][j]
    
    #left
    n_left = 0
    x = j-1
    while x >= 0 and M[i][x] < val:
        n_left += 1
        x = x - 1
    if x >= 0:
        n_left += 1
        
    #right
    n_right = 0
    x = j+1
    while x <= nb-1 and M[i][x] < val:
        n_right += 1
        x = x + 1
    if x <= nb-1:
        n_right += 1
        
    #up
    n_up = 0
    y = i-1
    while y >= 0 and M[y][j] < val:
        n_up += 1
        y = y - 1
    if y >= 0:
        n_up += 1
        
    #down
    n_down = 0
    y = i+1
    while y <= nb-1 and M[y][j] < val:
        n_down += 1
        y = y + 1
    if y <= nb-1:
        n_down += 1
        
    return n_left*n_right*n_up*n_down

#part2
print(max([max([view(i,j) for i in range(nb)]) for j in range(nb)]))
