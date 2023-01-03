data = open('input.txt').read().splitlines()
data = open('input_test.txt').read().splitlines()

line = 'Valve AA has flow rate=0; tunnels lead to valves DD, II, BB'

d = {}

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
    

for line in data:
    parse_line(line)
    

parcours = [('DD',1),
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
    minutes = 1
    opened = []
    while minutes <= 30:
        
        if parcours != []:
            action = parcours.pop()
            print("move to",action[0])
            if action[1] == 1:
                opened.append(action[0])
                minutes += 1
                print(minutes, 'open', action[0])
                print()
                pressure = sum([d[valve][0] for valve in opened])
                print("release", pressure)
                print()
                total_p += pressure
                minutes += 1
                print(minutes, total_p)
            else:
                pressure = sum([d[valve][0] for valve in opened])
                print("release", pressure)
                print()
                total_p += pressure
                minutes += 1
                print(minutes, total_p)
        else:
            pressure = sum([d[valve][0] for valve in opened])
            print("release", pressure)
            print()
            total_p += pressure
            minutes += 1
            print(minutes, total_p)
    return total_p


pression(parcours)