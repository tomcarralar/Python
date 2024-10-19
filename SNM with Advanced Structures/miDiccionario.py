class miDicc:
    def __init__(self, size):
        self.size = int(2*size)
        self.tablaD = self.consDicc()

    def consDicc(self): 
        return [None for _ in range(self.size)]

    def insert(self, key, val): 

        hKey = self.hash22(key) % self.size

        tabla = self.tablaD

        foundKey = False

        for index, record in enumerate(tabla, hKey): 

            if tabla[index] == None: 
                foundKey = True
                break
            
        if foundKey: 
            tabla[index] = (key, val)
        else: 
            for index, record in enumerate(tabla): 
                if record == None: 
                    tabla[index] = (key, val)
                    break

    def getValor(self, key):

        hKey = self.hash22(key) % self.size

        tabla = self.tablaD

        foundKey = False
        
        for index, record in enumerate(tabla, hKey): 
            if tabla[index] == None: break
            if tabla[index][0] == key: 
                foundKey = True
                break
            
        if foundKey: 
            return tabla[index][1]
        else: 
            return None

    
    def delKey(self, key):

        hKey = self.hash22(key) % self.size

        tabla = self.tablaD

        for index, record in enumerate(tabla, hKey):
            if tabla[index] == None: break

            if tabla[index][0] == key: 
                tabla[index] = None
                break

        return 
    def getS (self,i):
        return self.tablaD[i]

    def __str__(self):
        return "".join(str(item) for item in self.tablaD)

    def hash22(self, key): 
        num = key*key

        num = num / 17
        return int(num)
