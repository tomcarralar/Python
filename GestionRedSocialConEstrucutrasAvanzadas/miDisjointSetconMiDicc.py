from miArrayDeBits import *
from miDiccionario import *
class miDisjointSet(): 
    dicco =  miDicc(2000000)
    gr = miArrayDeBits(2000002)
    arrBy = miArrayDeBits(2000002)
    firstChild = miArrayDeBits(2000002)
    def __init__(self, n): 
        self.n = n
        
    '''
    Devuelve -1 si el usuario que envias no pertenece a ningun grupo
    '''
    @classmethod
    def mdsfind (self, user):
        padre =  self.dicco.getValor(user)
        if padre == None: 
            padre = -1
        return (padre)

    @classmethod
    def mdsFindGrum(self, i):
        grumo = self.arrBy.get(-i) 
        if grumo == None or i == -1:
            return -1
        elif grumo == i: 
            return (grumo)
        else:
            (grumo) = self.mdsFindGrum(grumo)
            self.arrBy.delKey(-i)
            self.arrBy.insert(-i, grumo)
            return (grumo)
    '''
    Dado un par de usuarios relacionados los pone en el grumo que corresponda
    '''
    @classmethod
    def mdsunion(self, user1, user2, indice):
        (padre1) = self.mdsfind(user1)
        grumoU1 = self.mdsFindGrum(padre1)
        (padre2) = self.mdsfind(user2)
        grumoU2 = self.mdsFindGrum(padre2)
        if padre1 == -1 and padre2 == -1:           # Cuando ninguno de los dos esta se crea un subgrumo, ojo varios sugrumos pueden pertencer al mismo grumo. 
            self.dicco.insert(user1, indice)
            self.dicco.insert(user2, indice)
            self.arrBy.insert(-indice, indice)
            self.gr.insert(-indice, 2)
            self.firstChild.insert(-indice, user1)
            indice = indice - 1
            return (indice)

        if grumoU1 == grumoU2 or padre1 == padre2:
            return (indice)            # Ambos usuarios ya tienen el mismo padre, luego son parte del mismo grumo
        
        if padre1 == -1:
            self.dicco.insert(user1, padre2)
            num_user = self.gr.get(-grumoU2) + 1
            self.gr.delKey(-grumoU2)
            self.gr.insert(-grumoU2, num_user)  
            return (indice)
        
        if padre2 == -1: 
            self.dicco.insert(user2, padre1)
            num_user = self.gr.get(-grumoU1) + 1
            self.gr.delKey(-grumoU1)
            self.gr.insert(-grumoU1, num_user) 
            return (indice)
        else:
            num_users2 = self.gr.get(-grumoU2)
            self.gr.delKey(-grumoU2)
            num_users = num_users2 + self.gr.get(-grumoU1)
            self.gr.delKey(-grumoU1)
            self.gr.insert(-grumoU1, num_users)
            self.arrBy.delKey(-grumoU2)
            self.arrBy.insert(-grumoU2, grumoU1)
            self.firstChild.delKey(-grumoU2)
            return (indice)

