import string
import pedina as pa
import numpy as np
NPEDINE = 10
NCOLONNE = 10
NRIGHE = 10


class board:
    def __init__(self):
        self.board = {}
        pass
    
    def posiziona_pedine(self):
        half_board = int(NRIGHE/2)
        start = 0
        
        for i in range(half_board - 1):
            for j in range(start, NCOLONNE, 2):
                self.board[(i, j)] = pa.pedinaX(i, j)
            start = not start
        
        start = 0
        for i in range(half_board + 1, NRIGHE):
            for j in range(start, NCOLONNE, 2):
                self.board[(i, j)] = pa.pedinaO(i, j)
            start = not start
            
    def move(self, i, j, d):
        if self.check_move(i, j, d):
            (newI, newJ) = self.board[(i, j)].move(d)
            self.board[newI, newJ] = self.board.pop((i, j))
            return True
        
        return False
            
    
    def check_move(self, i, j, d):
        if (i, j) in self.board:
            s = self.board[(i, j)].__str__()
            if s == "X":
                if d == "r" and (i+1, j+1) not in self.board:
                    return True
                
                elif d == "l" and (i+1, j-1) not in self.board:
                    return True
            elif s == "O":
                if d == "r" and (i-1, j+1) not in self.board:
                    return True
                
                elif d == "l" and (i-1, j-1) not in self.board:
                    return True
        
        return False
    
    def __str__(self):
        s =""
        m = np.full((NRIGHE, NCOLONNE), " ")
        k = self.board.keys()
        for i in k:
            m[i[0]][i[1]] = str(self.board[i])
        
        for i in range(NRIGHE-1, -1, -1):
            s += "|"
            for j in range(NCOLONNE):
                s +=  m[i][j] + "|"
            s += "\n"
            
        return s