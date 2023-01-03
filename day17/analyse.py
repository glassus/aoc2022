data = open('dic.txt').read().splitlines()

d = {}
for line in data:
    [k,v] = line.split(':')
    k = int(k)
    v = int(v)
    d[k] = v

def sol(v):
    return d[v]

def modulo(n):
    start = 11000
    return all([sol(start+(k+2)*n)-sol(start+(k+1)*n) == sol(start+(k+1)*n)-sol(start+(k+0)*n) for k in range(10)])



# for n in range(4000):
#     print(n)
#     if modulo(n):
#         print("trouvé", n)
#         #break
    
v = 1000000000000
s = 10040
p = 1720
nb = 581395343
val = 2738