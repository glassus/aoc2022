data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()


def convert(s):
    sol = 0
    n = len(s)
    for i in range(n):
        deg = n - 1 - i
        car = s[i]
        if car == "=":
            val = -2
        elif car == "-":
            val = -1
        else:
            val = int(car)
        sol += val * 5**deg
    return sol
        
sol = sum(convert(s) for s in data)
print(sol)


def five(a):
    bin_a = str(a%5)
    a = a // 5
    while a != 0 :
        bin_a = str(a%5) + bin_a
        a = a // 5
    return bin_a[::-1]



def snafu(n):
    sol = ""
    base = list(five(int(n)))
    long = len(base)
    i = 0
    while i < long:
        while base[i] in ('3', '4'):
            if base[i] == '3':
                sol += "="
                base = list(five(int(n)+2*5**i))
                if i == long-1:
                    long += 1
            if base[i] == '4':
                sol += "-"
                base = list(five(int(n)+1*5**i))
                if i == long-1:
                    long += 1
            i += 1
        if base[i] not in ('3', '4'):
            sol += base[i]
            i += 1    
#     if sol[-1] in ("-", "="):
#         sol += "1"
#         
#     elif sol[-2:] == "-2":
#         sol = sol[:-1] + "=1"
        
    return sol[::-1]
    
def test():    
    for k in range(1,10**3):
        if convert(snafu(k)) != k:
            print("erreur", k)
        print("ok")
    
    
def snaf(nb):
    s = five(nb)[::-1]
    n = len(s)
    l4 = []
    l3 = []
    for i in range(n):
        if s[i] == '4':
            l4.append(i)
        if s[i] == '3':
            l3.append(i)
    to_add = 0
    for e in l4:
        to_add += 5**(n-1-i)
    for e in l3:
        to_add += 2*5**(n-1-i)
    ns = five(nb + to_add)[::-1]
    
    lst = list(ns)
    for i in range(len(lst)):
        if lst[i] == '4':
            lst[i] = '-'
        if lst[i] == '3':
            lst[i] = '='
    return "".join(lst)
    
                      
        
    
    
    
    
    