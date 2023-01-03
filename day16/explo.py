a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], \
'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], \
'H':['','']}

def parcourir_arbre(noeud, valeurs):
  # Ajout de la valeur du noeud courant à la liste
  valeurs.append(noeud)

  # Parcours récursif des enfants du noeud courant
  if noeud != '':
      for enfant in a[noeud]:
        parcourir_arbre(enfant, valeurs)

# Utilisation de la fonction
valeurs = []
parcourir_arbre('F', valeurs)
print(valeurs)
