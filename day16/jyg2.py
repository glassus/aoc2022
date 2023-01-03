d = {'AA': [0, ['DD', 'II', 'BB']], 'BB': [13, ['CC', 'AA']],\
     'CC': [2, ['DD', 'BB']], 'DD': [20, ['CC', 'AA', 'EE']],\
     'EE': [3, ['FF', 'DD']], 'FF': [0, ['EE', 'GG']],\
     'GG': [0, ['FF', 'HH']], 'HH': [22, ['GG']], \
     'II': [0, ['AA', 'JJ']], 'JJ': [21, ['II']]}

def generer_mots(mot):    
    alphabet = d[mot[-1]][1]
    if all([lettre in mot for lettre in alphabet]):
        return None
    for lettre in alphabet:
        if lettre in mot:
            mots.append(mot)
            continue

        new_mot = mot[:]
        new_mot.append(lettre)
        generer_mots(new_mot)


mots = []
generer_mots(['AA'])
print(mots)

