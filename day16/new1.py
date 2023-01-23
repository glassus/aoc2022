from random import shuffle

data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

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
pos = [v for v in val if val[v] > 0 ]
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

parcours_1 = [('DD',1),
            ('AA',0),
            ('II',0),
            ('JJ',1),
            ('II',0),
            ('AA',0),
            ('BB',1),
            ('CC',1),
            ('DD',0),
            ('EE',1),
            ('FF',0),
            ('GG',0),
            ('HH',1)
            ]

parcours_2 = [('DD',1),
            ('AA',0),
            ('II',0),
            ('JJ',1)]

parcours_3 = [('DD',1),
            ('AA',0),
            ('BB',1)]


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

def road_to(start, goal):
    total = parcours_from(start)
    ind_min = 10**3
    for parc in total:
        if goal in parc:
            ind = parc.index(goal)
            if ind < ind_min:
                ind_min = ind
                good_parc = parc
    return good_parc[1:ind_min]

def make_trajet(etapes):
    traj = [('AA',0)]
    for ville in etapes:
        start = traj[-1][0]
        parc = road_to(start, ville)
        for city in parc:
            traj.append((city,0))
        traj.append((ville,1))
    return traj[1:]


def permut(lst, n):
    tot = []
    def gene(graine):
        if len(graine) == n:
            tot.append(graine)
            return None
        for k in lst:
            if k not in graine:
                gr = graine.copy()
                gr.append(k)
                gene(gr)
    gene([])
    return tot        
    
pos_triees = sorted(pos, key = lambda x : val[x], reverse = True)


def bf():
    tot = permut(pos_triees, len(pos_triees))
    mp = 0
    for parc in tot:
        p = pression(make_trajet(parc))
        if p > mp:
            mp = p
            max_parc = parc
    return max_parc, mp

def bfn(n):
    tot = permut(pos_triees, n)
    print("trajets analysés", len(tot))
    mp = 0
    for parc in tot:
        p = pression(make_trajet(parc))
        print(parc,p)
        if p > mp:
            mp = p
            max_parc = parc
    print(max_parc, mp)
