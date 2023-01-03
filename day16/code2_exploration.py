
data = open('input.txt').read().splitlines()
data = open('input_test.txt').read().splitlines()

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

