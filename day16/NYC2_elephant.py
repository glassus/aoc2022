from itertools import combinations

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


def pression(parcours):
    total_p = 0
    parcours.reverse()
    pressure = 0
    minutes = 0
    opened = []
    to_open = None
    while minutes < 26:
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


def n_parcours_from(start, n):
    total_parcours = []
    def parcours(graine):
        if len(graine) == n:
            total_parcours.append(graine)
            return None
        nxt = d[graine[-1]][1]
        for suiv in nxt:
            if suiv not in graine:
                cp_graine = list(graine)
                cp_graine.append(suiv)
                parcours(cp_graine)


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
        parc = mem_traj[(start, ville)]
        for city in parc:
            traj.append((city,0))
        traj.append((ville,1))
    return traj[1:]


def make_trajet_old(etapes):
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
        #print(parc,p)
        if p > mp:
            mp = p
            max_parc = parc
    print(max_parc, mp)
    
    
def bfn_list(valves, n=None):
    if n is None:
        n = len(valves)
    taille = 100
    lst = []
    tot = permut(valves, n)
    for parc in tot:
        if len(lst) < taille:
            lst.append((parc, pression(make_trajet(parc))))
        else:
            lst = sorted(lst, key = lambda x : x[1], reverse = True)
            p = pression(make_trajet(parc))
            if p > lst[-1][1]:
                lst.pop()
                lst.append((parc, pression(make_trajet(parc))))
    lst = sorted(lst, key = lambda x : x[1], reverse = True)
    return lst


mem_traj = {}
for dest in pos_triees:
    mem_traj[('AA', dest)] = road_to('AA', dest)

for origine in pos_triees:
    for dest in pos_triees:
        if dest != origine:
            mem_traj[(origine, dest)] = road_to(origine, dest)
        


def calc_best(valves):
    n = len(valves)
    if n < 7:
        return bfn_list(valves)[0]
        
    lst = bfn_list(valves, 5)
    for k in range(6, n+1):
        base = [v[0] for v in lst]
        new_best = []
        for parc in base:
            for valv in pos:
                if valv in parc:
                    continue
                cp = list(parc)
                cp.append(valv)
                new_best.append((cp, pression(make_trajet(cp))))
        new_best = sorted(new_best, key = lambda x : x[1], reverse = True)  
        lst = new_best[:10]
    return lst[0]


def best_repart():
    maxp = 0
    for comb in combinations(pos, 3):
        rest = [valv for valv in pos if valv not in comb]
        press = calc_best(comb)[1] + calc_best(rest)[1]
        if press > maxp:
            maxp = press
            best_comb = comb
    print(maxp, best_comb)
    
def repartition():
    lst_me = []
    poids_me = 0
    lst_elp = []
    poids_elp = 0
    for valv in pos_triees:
        if poids_me < poids_elp:
            lst_me.append(valv)
            poids_me += val[valv]
        else:
            lst_elp.append(valv)
            poids_elp += val[valv]
    return (lst_me, poids_me, lst_elp, poids_elp)



q = ['QO',  'FR',  'OF',  'VD',  'AJ',  'CG',  'AX',  'LM']
r = ['FV','GJ','RC','WI','ZR','KU','PI']
# 2497 too low


def poids_comb(comb):
    return sum([val[valve] for valve in comb])

def make_list_repart(nb):
    lst = []
    for comb in combinations(pos, 7):
        rest = [valv for valv in pos if valv not in comb]
        diff = abs(poids_comb(comb)-poids_comb(rest))
        tup = (comb, rest, diff)
        lst.append(tup)
    lst = sorted(lst, key = lambda x : x[2], reverse = False)
    return lst[:nb]

def best_cpl(lst):
    m = 0
    for cpl in lst:
        v = calc_best(cpl[0])[1] + calc_best(cpl[1])[1]
        if v > m:
            m = v
    return m