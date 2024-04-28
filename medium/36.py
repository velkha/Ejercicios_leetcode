""" No era comprobar solo los cuadrantes, si no la totalidad del sudoku
:type board: List[List[str]]
:rtype: bool
def isValidSudoku(self, board):
        
        :type board: List[List[str]]
        :rtype: bool
        
        i=0
        j=0
        while(i<=6):
            if not self.checkCuadrant(i,j,board):
                return False
            i += 3
        return True
    
    def checkCuadrant(self, i, j, board):
        auxDic = {}
        n = 0
        j = 0
        while(j<3):
            while (n<3):
                print(board[i+n][j])
                if(board[i+n][j] in auxDic):
                    return False
                elif(board[i+n][j] != "."):
                    print("Saving")
                    print(board[i+n][j])
                    auxDic[board[i+n][j]] = 1
                n+=1
            j+=1
            n=0
        return len(auxDic)>0
"""
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        Se me ha cerretido el cerebro en el proceso de hacer el sudoku, pero la idea es que se recorre el tablero
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        cuadrant = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    cuadrant_index = (i // 3) * 3 + (j // 3)
                    if num in rows[i] or num in cols[j] or num in cuadrant[cuadrant_index]:
                        return False
                    rows[i].add(num)
                    cols[j].add(num)
                    cuadrant[cuadrant_index].add(num)
        return True