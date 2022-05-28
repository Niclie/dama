class pedina:
    
    def __init__(self, s, i, j):
        self.s = s
        self.i = i
        self.j = j
        
    def __str__(self):
        return self.s
    
    def getI(self):
        return self.i
    
    def getJ(self):
        return self.j
        
        
class pedinaX(pedina):
    
    def __init__(self, i, j):
        super().__init__("X", i, j)
        
    def move(self, d):
        self.i +=1
        
        if d == "r":
            self.j += 1
        elif d == "l":
            self.j -= 1

        return (self.i, self.j)
            
            
            
            
            
class pedinaO(pedina):
    
    def __init__(self, i, j):
        super().__init__("O", i, j)
        
    def move(self, d):
        self.i -= 1
        
        if d == "r":
            self.j += 1
        elif d == "l":
            self.j -= 1
            
        return (self.i, self.j)
        
