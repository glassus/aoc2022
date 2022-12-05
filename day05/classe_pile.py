class Pile:
    def __init__(self):
        self.data = []

    def est_vide(self):
        return len(self.data) == 0 


    def empile(self,x):
        self.data.append(x)

    def depile(self):
        if self.est_vide():
            print('Vous avez essayé de dépiler une pile vide !')
            return None
        else :
            return self.data.pop()
    
    def sommet(self):
        if self.est_vide():
            return ''
        elt = self.depile()
        self.empile(elt)
        return elt

    def __str__(self):       # Hors-Programme : pour afficher 
        s = '|'              # convenablement la pile avec print(p)
        for k in self.data :
            s = s + str(k) + '|'
        return s

    def __repr__(self):       # Hors-Programme : pour afficher 
        s = '|'              # convenablement la pile avec p
        for k in self.data :
            s = s + str(k) + '|'
        return s  
