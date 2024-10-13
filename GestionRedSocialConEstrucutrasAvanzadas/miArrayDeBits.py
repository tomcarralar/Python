class miArrayDeBits(): 

    def __init__(self, size):
        self.size = size
        self.tablaD = [None for _ in range(self.size)]

    def insert(self, key, val):
        self.tablaD[key] = (val)

    def get(self, key):
        return self.tablaD[key]

    def delKey(self, key): 
        self.tablaD[key] = None
    def __str__(self):
        return "".join(str(item) for item in self.tablaD)
'''
tabla = miArrayDeBits(50)

tabla.insert(43, 432)
tabla.insert(42, 53)
tabla.delKey(43)
print(tabla.tablaD, tabla.get(2))
'''