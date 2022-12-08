import time
t0 = time.time()

data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

class Dir:
    def __init__(self, name):
        self.name = name
        self.files = {}
        self.children = []
        self.parent = None
        

lst_dir = []
lst_dir.append(Dir('racine'))

cwd = lst_dir[0]

for line in data:
    if line in ['$ cd /', '$ ls']:
        continue
    mots = line.split()
    if mots[0] == 'dir':
        name = mots[1]
        new_dir = Dir(name)
        lst_dir.append(new_dir)
        cwd.children.append(new_dir)
        new_dir.parent = cwd
        
    elif mots[0] == '$' and mots[1] == 'cd':
        if mots[2] == '..':
            cwd = cwd.parent
        else:
            for rep in cwd.children:
                if rep.name == mots[2]:
                    next_dir = rep
            cwd = next_dir
    else:
        cwd.files[mots[1]] = int(mots[0])

def aff():
    for rep in lst_dir:
        print(rep.name, rep.files, rep.children, rep.parent)
        
# fonction poids en récursif + mémoïsation
dic_poids = {}
def poids(rep):
    if rep in dic_poids:
        return dic_poids[rep]
    total_files = sum([rep.files[f] for f in rep.files])
    if rep.children == []:
        return total_files
    else:
        val = total_files + sum([poids(child) for child in rep.children])
        dic_poids[rep] = val
        return val








# #part1
# t = 0
# for rep in lst_dir:
#     p = poids(rep)
#     if p <= 100000:
#         t += p
# print(t)

# part 2

free = 70000000 - poids(lst_dir[0])
to_free = 30000000 - free

rank = [poids(rep) for rep in lst_dir]
rank.sort()

def sol():
    for r in rank:
        if r > to_free:
            return r
print(sol())
print(time.time()-t0)