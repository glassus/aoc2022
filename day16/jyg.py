a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], \
'C':['',''], 'E':['',''], 'G':['I',''], 'I':['','H'], \
'H':['','']}




def generer_mots(graine):
    suivants  = a[graine[-1]]

    for fils in suivants:
        if fils != '':
            nxt_graine = list(graine)
            nxt_graine.append(fils)
            generer_mots(nxt_graine)
    
    for fils in suivants:
        if fils == '':
            mots.append(graine)
            return None
     
mots = []
generer_mots(['F'])
print(mots)
