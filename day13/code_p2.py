from code import compare

data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

data.append('[[2]]')
data.append('[[6]]')
ind = 0
for i in range(len(data)):
    if data[i] == '':
        ind += 1
for _ in range(ind):
    data.remove('')



def tri_selection(lst) :
    for k in range(len(lst)-1):
        indice_min = k
        for i in range(k+1, len(lst)) :
            if compare(lst[i],lst[indice_min]):
                indice_min = i
        lst[k], lst[indice_min] = lst[indice_min], lst[k]
        
tri_selection(data)

i1 = data.index('[[2]]') + 1
i2 = data.index('[[6]]') + 1

print(i1*i2)




        

