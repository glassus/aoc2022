data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

class Maillon:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.nxt = None
        
lst = [int(n) for n in data]
lst = [int(n)*811589153 for n in data]



d = {}
for i, val in enumerate(lst):
    d[i] = Maillon(val)

start = d[0]


for i in range(1, len(data)-1):
    d[i].prev = d[i-1]
    d[i].nxt = d[i+1]
d[len(data)-1].nxt = d[0]
d[len(data)-1].prev = d[len(data)-2]
d[0].prev = d[len(data)-1]
d[0].nxt = d[1]



def move(maillon, n):
    if n == 0:
        return None
    if n > 0 and n % (len(lst)-1) == 0:
        return None
    if n < 0 and (abs(n)+1)%(len(lst)-1) == 0:
        return None
    tgt = maillon
    if n > 0:
        for _ in range(abs(n)%(len(lst)-1)):
            tgt = tgt.nxt
    if n < 0:
        for _ in range(1+abs(n)%(len(lst)-1)):
            tgt = tgt.prev

    maillon.prev.nxt = maillon.nxt
    maillon.nxt.prev = maillon.prev
    maillon.nxt = tgt.nxt
    tgt.nxt.prev = maillon
    tgt.nxt = maillon
    maillon.prev = tgt
   

def aff():
    maillon = d[0]
    for _ in range(len(data)):
        print(maillon.val, end = ', ')
        maillon = maillon.nxt
        
def ronde():
    for i in range(len(data)):
        move(d[i], d[i].val)


def after_zero(n):
    maillon = d[lst.index(0)]
    for _ in range(n):
        maillon = maillon.nxt
    return maillon.val

#aff()
#print()
for _ in range(10):
    ronde()
    #aff()
    #print()
print(after_zero(1000) + after_zero(2000) + after_zero(3000))
