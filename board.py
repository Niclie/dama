from sympy import false
import pedina as pa
import  itertools as it
NPEDINE = 10
NCOLONNE = 10
NRIGHE = 10


class board:
    def __init__(self):
        self.board = {}
        pass
    
    def posiziona_pedine(self):
        half_board = int(NRIGHE/2)
        bool = False
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
                