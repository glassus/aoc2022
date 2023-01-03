from random import choice

data = open('input.txt').read().splitlines()
data = open('input_test.txt').read().splitlines()

line = 'Valve AA has flow rate=0; tunnels lead to valves DD, II, BB'

d = {}
val = {}



def parse_line(line):
    if 'tunnels' in line:
        l = line.split('; tunnels lead to valves ')
    else:
        l = line.split('; tunnel leads to valve ')
    v = l[1].split(', ')
    l = l[0].split(' has flow rate=')
    r = int(l[1])
    valv = l[0].split('Valve ')[1]
    d[valv] = [r,v]
    val[valv] = r
    
def init():
    for line in data:
        parse_line(line)

init()
nb_pos = sum([val[v] > 0 for v in val])


parcours_or = [('DD',1),
            ('CC',0),
            ('BB',1),
            ('AA',0),
            ('II',0),
            ('JJ',1),
            ('II',0),
            ('AA',0),
            ('DD',0),
            ('EE',0),
            ('FF',0),
            ('GG',0),
            ('HH',1),
            ('GG',0),
            ('FF',0),
            ('EE',1),
            ('DD',0),
            ('CC',1)
            ]

def pression(parcours):
    total_p = 0
    parcours.reverse()
    pressure = 0
    minutes = 0
    opened = []
    to_open = None
    while minutes < 30:
        minutes += 1
        #print("minutes", minutes, "opened", opened)
        pressure = sum([d[valve][0] for valve in opened])
        total_p += pressure
        #print(pressure)
        if to_open is not None:
            opened.append(to_open)
            to_open = None
            continue        
        if parcours != []:
            action = parcours.pop()
            if action[1] == 1:
                ouvert = True
                to_open = action[0]
                continue        
    return total_p


def suivante(valve):
    candidats = d[valve][1]
    # pure random
    return choice(candidats)
 
    # si tous les valves à venir sont nulles...
    if sum([val[c] for c in candidats]) == 0:
        # on choisit celle qui a un truc non nul derrière
        for c in candidats:
            for suiv in d[c][1]:
                if val[suiv] > 1:
                    return c
        # ou bien au hasard
        return choice(candidats)
    # si y a le choix on prend la meilleure
    candidats_classes = sorted(candidats, key = lambda x: val[x])
    return candidats_classes[-1]

def choix_ouv(valve, opened):
    if valve in opened:
        return 0
    if val[valve] != 0:
        #return choice([0,1])
        return 1
    else:
        return 0

def parcours():
    valve = 'AA'
    parc = []
    opened = []
    while len(opened) != nb_pos and len(parc) + len(opened) <= 30:
        valve = suivante(valve)
        decision = choix_ouv(valve, opened)
        if decision == 1:
            opened.append(valve)
            val[valve] = 0
        parc.append((valve, decision))
    return parc

def search():
    m = 0
    timing = 0
    for _ in range(10**6):
        init()
        p = parcours()
        p_temp = list(p)
        v = pression(p)
        #print(v)
        if v > m:
            m = v
            timing = 0
    print(m)
    
# m = parcours()
# print(m)
# print(pression(m))

#search()