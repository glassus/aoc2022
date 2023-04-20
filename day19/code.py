data = open('input.txt').read().splitlines()
data = open('input_test.txt').read().splitlines()

t = "Blueprint 2: Each ore robot costs 4 ore. Each clay robot costs 4 ore.\
Each obsidian robot costs 3 ore and 19 clay. Each geode robot costs 4 ore and 15 obsidian."

blueprint = {}

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
    blueprint[v[0]] = v[1:]

def affiche(minute, etat):
    nb_ore, nb_clay, nb_obs, nb_geo, nb_rob_ore, nb_rob_clay, nb_rob_obs, nb_rob_geo = etat
    print("\n minutes :",minute, \
          " \n nb_ores :", nb_ore, \
          " \n nb_clay :", nb_clay, \
          "\n nb_rob_ore :", nb_rob_ore, \
          "\n nb_rob_clay :", nb_rob_clay, \
          "\n nb_rob_obs :", nb_rob_obs
          )

def deroule(k):
    pr_rob_ore,\
    pr_rob_clay, \
    pr_rob_obs_ore, \
    pr_rob_obs_clay, \
    pr_rob_geo_ore, \
    pr_rob_geo_clay = blueprint[k]
    
    nb_ore, nb_clay, nb_obs, nb_geo = 0, 0, 0, 0
    nb_rob_ore, nb_rob_clay, nb_rob_obs, nb_rob_geo = 1, 0, 0, 0
    
    minute = 0
    while minute < 10:
        
        if nb_clay >= pr_rob_obs_clay and \
           nb_ore >= pr_rob_obs_ore:
            nb_clay -= pr_rob_obs_clay
            nb_ore -= pr_rob_obs_ore
            rob_obs_to_add = 1
        else:
            rob_obs_to_add = 0
        
        
        if nb_ore >= pr_rob_clay:
            nb_ore -= pr_rob_clay
            rob_clay_to_add = 1
        else:
            rob_clay_to_add = 0     
            

            
        nb_ore += nb_rob_ore
        nb_clay += nb_rob_clay
        
        nb_rob_clay += rob_clay_to_add
        nb_rob_obs += rob_obs_to_add
        
        minute += 1
        affiche(minute, etat)
    
deroule(1) 
    