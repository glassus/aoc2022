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


parcours_opt = [('DD',1),
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


def parcours_from(start):
    total_parcours = []
    def parcours(graine):
        nxt = d[graine[-1]][1]
        for suiv in nxt:
            if suiv not in graine:
                cp_graine = list(graine)
                cp_graine.append(suiv)
                parcours(cp_graine)

        if all([suiv in graine for suiv in nxt]):
                total_parcours.append(graine)
                return None
    parcours([start])
    return total_parcours
    

def best_from(start, curr_time):
    parcours = parcours_from(start)
    best_pot = 0
    best_pos = ''
    best_parc = []
    step = 0
    for parc in parcours:
        for i, pos in enumerate(parc):
            pot = val[pos]*(30-curr_time-i)
            if pot > best_pot:
                best_pot = pot
                best_pos = pos
                best_parc = parc
                step = i
    return best_pos, best_parc[1:step], step

def second_best_from(start, curr_time):
    fbest_pos, _, _ = best_from(start, curr_time)
    parcours = parcours_from(start)
    best_pot = 0
    best_pos = ''
    best_parc = []
    step = 0
    for parc in parcours:
        for i, pos in enumerate(parc):
            pot = val[pos]*(30-curr_time-i)
            if pot > best_pot and pos != fbest_pos:
                best_pot = pot
                best_pos = pos
                best_parc = parc
                step = i
    return best_pos, best_parc[1:step], step


def best_parc():
    curr = 0
    best = []
    pos = 'AA'
    while curr <= 30:
        print(pos, curr, best)
        best.append((pos,1))
        best_pos, best_parc, step = best_from(pos, curr)
        val[best_pos] = 0
        curr += step + 1
        pos = best_pos
        for p in best_parc:
            best.append((p,0))
        
p = [('AA', 0), ('II', 0), ('JJ', 1), ('II', 0), ('AA', 0), ('DD', 1), ('EE', 0), ('FF', 0), ('GG', 0), ('HH', 1), ('GG', 0), ('FF', 0), ('EE', 0), ('DD', 0), ('CC', 0), ('BB', 1), ('CC', 0), ('DD', 0), ('EE', 1), ('DD', 0), ('CC', 1)]