data = open('input.txt').read().splitlines()
data = open('input_test.txt').read().splitlines()

c = {}
d = {}

for line in data:
    if "+" in line:
        l = line.split(': ')
        v = l[0]
        [a, b] = l[1].split(' + ')
        d[v] = (a,b,'+')
    elif "-" in line:
        l = line.split(': ')
        v = l[0]
        [a, b] = l[1].split(' - ')
        d[v] = (a,b,'-')
    elif "*" in line:
        l = line.split(': ')
        v = l[0]
        [a, b] = l[1].split(' * ')
        d[v] = (a,b,'*')
    elif "/" in line:
        l = line.split(': ')
        v = l[0]
        [a, b] = l[1].split(' / ')
        d[v] = (a,b,'/')
    else:
        v = line.split(': ')[0]
        n = int(line.split(': ')[1])
        c[v] = n
        
def simp(name):
    n1, n2, op = d[name][0], d[name][1], d[name][2]
    if n1 in c and n2 in c:
        if op == '+':
            val = c[n1] + c[n2]
        elif op == '-':
            val = c[n1] - c[n2]
        elif op == '*':
            val = c[n1] * c[n2]
        elif op == '/':
            val = c[n1] / c[n2]
        c[name] = val
        return name
    return None

while len(d) > 0:
    to_del = []
    for name in d:
        v = simp(name)
        if v:
            to_del.append(v)
    for name in to_del:
        del d[name]

print(c['root'])
    
    
    
    