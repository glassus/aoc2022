data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

class Maillon:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.nxt = None
        
lst = [int(n) for n in data]
d = {}
for s in data:
    n = int(s)
    d[n] = Maillon(n)

for i in range(len(data)-1):
    d[int(data[i])].prev = d[int(data[i-1])]
    d[int(data[i])].nxt = d[int(data[i+1])]
d[int(data[len(data)-1])].nxt = d[int(data[0])]
d[int(data[len(data)-1])].prev = d[int(data[len(data)-2])]



def move(maillon, n):
    if n == 0:
        return None
    tgt = maillon.val
    if n > 0:
        for _ in range(abs(n)):
            tgt = d[tgt].nxt.val
    if n < 0:
        for _ in range(abs(n)+1):
            tgt = d[tgt].prev.val

    maillon.prev.nxt = maillon.nxt
    maillon.nxt.prev = maillon.prev
    maillon.nxt = d[tgt].nxt
    d[tgt].nxt.prev = maillon
    d[tgt].nxt = maillon
    maillon.prev = d[tgt]
   

def aff():
    val = 1
    for _ in range(len(data)):
        print(val, end = ', ')
        val = d[val].nxt.val
        
def ronde():
    for val in lst:
        move(d[val],val)


def after_zero(n):
    val = 0
    for _ in range(n):
        val = d[val].nxt.val
    return val

ronde()
print(after_zero(1000) + after_zero(2000) + after_zero(3000))
