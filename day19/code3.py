data = open('input.txt').read().splitlines()
data = open('input_test.txt').read().splitlines()

class Blueprint:
    def __init__(self, id, pr_rob_ore, pr_rob_clay, pr_rob_obs_ore, pr_rob_obs_clay, pr_rob_geo_ore, pr_rob_geo_obs):
        self.id = id
        self.pr_rob_ore = pr_rob_ore
        self.pr_rob_clay = pr_rob_clay
        self.pr_rob_obs_ore = pr_rob_obs_ore
        self.pr_rob_obs_clay = pr_rob_obs_clay
        self.pr_rob_geo_ore = pr_rob_geo_ore
        self.pr_rob_geo_obs = pr_rob_geo_obs
        
class Etat:
    def __init__(self):
        self.nb_ore = 0
        self.nb_clay = 0
        self.nb_obs = 0
        self.nb_geo = 0
        self.nb_rob_ore = 1
        self.nb_rob_clay = 0
        self.nb_rob_obs = 0
        self.nb_rob_geo = 0
        
        
        
def changed(e):
    ne = Etat()
    ne.nb_ore = e.nb_ore
    ne.nb_clay = e.nb_clay
    ne.nb_obs = e.nb_obs
    ne.nb_geo = e.nb_geo
    ne.nb_rob_ore = e.nb_rob_ore
    ne.nb_rob_clay = e.nb_rob_clay
    ne.nb_rob_obs = e.nb_rob_obs
    ne.nb_rob_geo = e.nb_rob_geo
    
    ne.nb_ore += e.nb_rob_ore
    ne.nb_clay += e.nb_rob_clay
    ne.nb_obs += e.nb_rob_obs
    ne.nb_geo += e.nb_rob_geo
    return ne
    



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

def affiche(minute, e):
    print("\n minutes :", minute, \
          " \n nb_ores :", e.nb_ore, \
          " \n nb_clay :", e.nb_clay, \
          " \n nb_obs :", e.nb_obs, \
          " \n nb_geo :", e.nb_geo, \
          "\n nb_rob_ore :", e.nb_rob_ore, \
          "\n nb_rob_clay :", e.nb_rob_clay, \
          "\n nb_rob_obs :", e.nb_rob_obs
          )

def possible_const_rob_ore(blueprint, e):
    return e.nb_ore >= blueprint.pr_rob_ore

def change_const_rob_ore(blueprint, e):
    e.nb_ore -= blueprint.pr_rob_ore
    e.nb_rob_ore += 1
    return e


def possible_const_rob_clay(blueprint, e):
    return e.nb_ore >= blueprint.pr_rob_obs_clay

def interet_const_rob_clay(blueprint, e):
    return e.nb_clay < blueprint.pr_rob_obs_clay

def change_const_rob_clay(blueprint, e):
    e.nb_ore -= blueprint.pr_rob_clay
    e.nb_rob_clay += 1
    return e

def possible_const_rob_obs(blueprint, e):
    return e.nb_clay >= blueprint.pr_rob_obs_clay and e.nb_ore >= blueprint.pr_rob_obs_ore

def interet_const_rob_obs(blueprint, e):
    return e.nb_obs < blueprint.pr_rob_geo_obs
           
def change_const_rob_obs(blueprint, e):
    e.nb_clay -= blueprint.pr_rob_obs_clay
    e.nb_ore -= blueprint.pr_rob_obs_ore
    e.nb_rob_obs += 1
    return e
                  
def possible_const_rob_geo(blueprint, e):
    return e.nb_obs >= blueprint.pr_rob_geo_obs and e.nb_ore >= blueprint.pr_rob_geo_ore  

def change_const_rob_geo(blueprint, e):
    e.nb_obs -= blueprint.pr_rob_geo_obs
    e.nb_ore -= blueprint.pr_rob_geo_ore
    e.nb_rob_geo += 1
    return e

m = [0,0,0,0]
mem = [0]

def deroule(blueprint, minute, etat):
    
    if minute == 24:
        if etat.nb_geo > m[0]:
            m[0] = etat.nb_geo
            mem[0] = etat
        return None
    
    
    
    if possible_const_rob_geo(blueprint, etat):
        deroule(blueprint, minute+1, change_const_rob_geo(blueprint, changed(etat)))
    
    elif interet_const_rob_obs(blueprint, etat) and possible_const_rob_obs(blueprint, etat):
        deroule(blueprint, minute+1, change_const_rob_obs(blueprint, changed(etat)))
        
    elif interet_const_rob_clay(blueprint, etat) and possible_const_rob_clay(blueprint, etat):
        deroule(blueprint, minute+1, change_const_rob_clay(blueprint, changed(etat)))

    elif possible_const_rob_ore(blueprint, etat):
        deroule(blueprint, minute+1, change_const_rob_ore(blueprint, changed(etat)))
 
    else:
        deroule(blueprint, minute+1, changed(etat))

b = blueprints[1]
etat = Etat()
deroule(b, 0, etat)
for e in mem:
    print(e.nb_ore, e.nb_clay, e.nb_obs, e.nb_geo)

print(m)
    