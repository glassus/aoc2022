data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()
#data = ['noop','addx 3','addx -5']

instructions = []
for line in data:
    if 'noop' in line:
        instructions.append([0,1])
    else:
        val = int(line.split()[1])
        instructions.append([val,2])

instructions.reverse()

X = 1
cycle_next_inst = 1
to_add = 0
signal_strength = 0

crt = ['.']*240

for cycle in range(1,241):
    pos_draw = (cycle-1) % 40 

    if cycle == cycle_next_inst:
        X += to_add
        inst = instructions.pop()
        cycle_next_inst += inst[1]
        to_add = inst[0]
        
    if (cycle-20) % 40 == 0:
        signal_strength += cycle*X
    
    if pos_draw - X in (-1,0,1):
        crt[cycle-1] = '#'

#part1
#print(signal_strength)

#part2
for k in range(6):        
    print(''.join(crt[40*k:40*(k+1)]))

