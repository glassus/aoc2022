from copy import deepcopy

data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

class Blueprint:
    def __init__(self, id, pr_rob_ore, pr_rob_clay, pr_rob_obs_ore, pr_rob_obs_clay, pr_rob_geo_ore, pr_rob_geo_obs):
        self.id = id
        self.pr_rob_ore = pr_rob_ore
        self.pr_rob_clay = pr_rob_clay
        self.pr_rob_obs_ore = pr_rob_obs_ore
        self.pr_rob_obs_clay = pr_rob_obs_clay
        self.pr_rob_geo_ore = pr_rob_geo_ore
        self.pr_rob_geo_obs = pr_rob_geo_obs
        

blueprints = []

def parse(line):
    line = line.replace("Blueprint ", "")
    line = line.replace(": Each ore robot costs ", ",")
    line = line.replace(" ore. Each clay robot costs ", ",")
    line = line.replace(" ore. Each obsidian robot costs ", ",")
    line = line.replace(" ore and ", ",")
    line = line.replace(" clay. Each geode robot costs ", ",")
    line = line.replace(" obsidian.", "")
    v = [int(k) for k in line.split(',')]
    return v

for line in data:
    v = parse(line)
    blueprints.append(Blueprint(*v))

def interet_const_rob_ore(blueprint, e):
    return e[4] < max(blueprint.pr_rob_ore, blueprint.pr_rob_clay, blueprint.pr_rob_obs_ore, blueprint.pr_rob_geo_ore)

def possible_const_rob_ore(blueprint, e):
    return e[0] >= blueprint.pr_rob_ore

def change_const_rob_ore(blueprint, e):
    e[0] -= blueprint.pr_rob_ore
    e[4] += 1
    return e


def interet_const_rob_clay(blueprint, e):
    return e[5] < blueprint.pr_rob_obs_clay

def possible_const_rob_clay(blueprint, e):
    return e[0] >= blueprint.pr_rob_clay

def change_const_rob_clay(blueprint, e):
    e[0] -= blueprint.pr_rob_clay
    e[5] += 1
    return e


def interet_const_rob_obs(blueprint, e):
    return e[6] < blueprint.pr_rob_geo_obs

def possible_const_rob_obs(blueprint, e):
    return e[1] >= blueprint.pr_rob_obs_clay and e[0] >= blueprint.pr_rob_obs_ore
           
def change_const_rob_obs(blueprint, e):
    e[1] -= blueprint.pr_rob_obs_clay
    e[0] -= blueprint.pr_rob_obs_ore
    e[6] += 1
    return e
                  
def possible_const_rob_geo(blueprint, e):
    return e[2] >= blueprint.pr_rob_geo_obs and e[0] >= blueprint.pr_rob_geo_ore  

def change_const_rob_geo(blueprint, e):
    e[2] -= blueprint.pr_rob_geo_obs
    e[0] -= blueprint.pr_rob_geo_ore
    e[7] += 1
    return e


    
    

b = blueprints[0]

def avance(lst):
    new = deepcopy(lst)
    new[0] += new[4]
    new[1] += new[5]
    new[2] += new[6]
    new[3] += new[7]
    return new


def score(c, blueprint):
    return 10*abs(c[4]-blueprint.pr_rob_ore) + 10*abs(c[5]-blueprint.pr_rob_obs_clay) \
           + 100*abs(c[4]-blueprint.pr_rob_geo_obs)
    
def mot(lst):
    return "".join(str(k) for k in lst)
    
    
start = [0,0,0,0,1,0,0,0]

pile = [start]

for i in range(32):
    to_add = []
    set_ta = set()
    print(i, len(pile))
    while pile != []:
        curr = pile.pop()
        
        if possible_const_rob_geo(b, curr):
            c = change_const_rob_geo(b, avance(curr))
            if mot(c) not in set_ta:
                to_add.append(c)
                set_ta.add(mot(c))
            

        
        else:
            if possible_const_rob_obs(b, curr):
                c = change_const_rob_obs(b, avance(curr))
                if mot(c) not in set_ta:
                    to_add.append(c)
                    set_ta.add(mot(c))
    
            if interet_const_rob_clay(b, curr) and possible_const_rob_clay(b, curr):
                c = change_const_rob_clay(b, avance(curr))
                if mot(c) not in set_ta:
                    to_add.append(c)
                    set_ta.add(mot(c))
                
            if interet_const_rob_ore(b, curr) and possible_const_rob_ore(b, curr):
                c = change_const_rob_ore(b, avance(curr))
                if mot(c) not in set_ta:
                    to_add.append(c)
                    set_ta.add(mot(c))
            
            c = avance(curr)
            if mot(c) not in set_ta:
                to_add.append(c)
                set_ta.add(mot(c))
    
    if i > 10:
        k = 500000
#         #best_ore = sorted(to_add, key =  lambda x : x[4], reverse = True)[:k]
#         #best_clay = sorted(to_add, key =  lambda x : x[5], reverse = True)[:k]
# #         best_obs = sorted(to_add, key =  lambda x : x[2], reverse = True)[:k]
# #         best_geo = sorted(to_add, key =  lambda x : x[3], reverse = True)[:k]
        #to_add = sorted(to_add, key =  lambda x : x[0], reverse = True)
        #to_add = sorted(to_add, key =  lambda x : x[1], reverse = True)
        to_add = sorted(to_add, key =  lambda x : x[2], reverse = True)
        to_add = sorted(to_add, key =  lambda x : x[3], reverse = True)[:k]
        
        
        #to_add = sorted(to_add, key =  lambda x : score(x, b), reverse = False)[:k]
        
         #to_add = best_obs + best_clay + best_geo + best_ore
        #to_add = best_rob_clay + best_rob_obs + best_rob_geo 
        
    pile = deepcopy(to_add)
    
def max_geo(pile):
    return max([lst[3] for lst in pile])
    
    
print(max_geo(pile))

    