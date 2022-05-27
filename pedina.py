class pedina:
    
    def __init__(self, s, x, y):
        self.s = s
        self.x = x
        self.y = y
        
    
        
        
        
class pedinaX(pedina):
    
    def __init__(self, x, y):
        super().__init__("X", x, y)
        
    def move(self, d):
        if d == "r":
            self.y += 1
        elif d == "l":
            self.y -= 1
        
        self.x +=1        
            
            
            
            
            
class pedinaO(pedina):
    
    def __init__(self, x, y):
        super().__init__("O", x, y)
        
    def move(self, d):
        if d == "r":
            self.x += 1
        elif d == "l":
            self.x -= 1
        
        self.y -= 1
        
