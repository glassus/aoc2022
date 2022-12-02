data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

#   X Y Z
# A 3 0 6
# B 6 3 0
# C 0 6 3

game = [[3, 6, 0],
        [0, 3, 6],
        [6, 0, 3]]

def conv(s):
    v1 = ord(s[0]) - ord('A')
    v2 = ord(s[-1]) - ord('X')
    return (v1, v2)

def points(s):
    p_jeu = game[conv(s)[0]][conv(s)[1]]
    p_choix = ord(s[-1]) - ord('X') + 1
    return p_jeu + p_choix

#part1
scores = [points(s) for s in data]
sol = sum(scores)
print(sol)


#part2

#   X Y Z
# A Z X Y
# B X Y Z
# C Y Z X

play = [['Z', 'X', 'Y'],
        ['X', 'Y', 'Z'],
        ['Y', 'Z', 'X']]

def new_s(s):
    v1 = ord(s[0]) - ord('A')
    v2 = ord(s[-1]) - ord('X')
    to_play = play[v1][v2]
    return s[:-1] + to_play

scores = [points(new_s(s)) for s in data]
sol = sum(scores)
print(sol)
    