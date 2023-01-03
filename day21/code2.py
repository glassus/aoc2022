data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

c = {}
d = {}

def init():
    c, d = {}, {}
    for line in data:
#         if 'root' in line:
#             continue
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
    return c, d

            
def simp(name, c, d):
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

def compare(mot, val):
    c, d = init()
    d_sauv = dict(d)
    c['humn'] = val
    while len(d) > 0:
        to_del = []
        for name in d:
            v = simp(name, c, d)
            if v:
                to_del.append(v)
        for name in to_del:
            del d[name]
    
    (m1, m2, _) = d_sauv[mot]
    return c[m1], c[m2], d_sauv

# wrvq, 94625185243550
def target(mot, val):
    (v0, v1, d) = compare(mot, 10)
    (w0, w1, _) = compare(mot, 72)
    if v0 == w0:
        nxt_tgt = d[mot][1]
        op = d[mot][2]
        if op == "+":
            nxt_val = val - v0
        elif op == "-":
            nxt_val = v0 - val   
        elif op == "*":
            nxt_val = val / v0
        elif op == "/":
            nxt_val = v0 / val
    else:
        nxt_tgt = d[mot][0]
        op = d[mot][2]
        if op == "+":
            nxt_val = val - v1
        elif op == "-":
            nxt_val = v1 + val   
        elif op == "*":
            nxt_val = val / v1
        elif op == "/":
            nxt_val = v1 * val
    return nxt_tgt, nxt_val
        

#wrvq, 94625185243550
(mot, val) = ('wrvq',94625185243550)
while mot != 'humn':
    nm, nv = target(mot,val)
    print(nm, nv)
    mot, val = nm, nv
    
    
    