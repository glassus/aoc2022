data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()
data.append('')

L = '[[[],5,4,7,[[9,5,9],[]]]]'
R = '[[10,[1,[2,3],9,[3]]],[[[5,7,9,10,8],[]],0]]'




def compare(L, R):
    L = list(L)
    R = list(R)
    L.reverse()
    R.reverse()
    
    while L != [] and R != []:
        l = L.pop()
        r = R.pop()
        
        if ord(l) in range(48,58) and r == '[':
            nl = L.pop()
            if ord(nl) in range(48,58):
                l = l + nl
            else:
                L.append(nl)
            
            L.append(']')
            if len(l) == 2:
                L.append(l[1])
            L.append(l[0])
            L.append('[')
            R.append(r)
            continue

        if ord(r) in range(48,58) and l == '[':
            nr = R.pop()
            if ord(nr) in range(48,58):
                r = r + nr
            else:
                R.append(nr)
            
            R.append(']')
            if len(r) == 2:
                R.append(r[1])
            R.append(r[0])
            R.append('[')
            L.append(l)
            continue     
        
        if ord(l) in range(48,58):
            nl = L.pop()
            if ord(nl) in range(48,58):
                l = l + nl
            else:
                L.append(nl)

        if ord(r) in range(48,58):
            nr = R.pop()
            if ord(nr) in range(48,58):
                r = r + nr
            else:
                R.append(nr)
        
        if l == r:
            continue
        
        if l != ']' and r == ']':
            return False           
            
        if l == ']' and r != ']':
            return True             
        
        if int(l) < int(r):
            return True
        else:
            return False



def sol():
    somme = 0
    nbl = len(data) // 3
    for k in range(nbl):
        L = data[3*k]
        R = data[3*k+1]
        if compare(L,R):
            somme += k+1
    print(somme)

