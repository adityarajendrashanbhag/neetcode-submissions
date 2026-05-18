class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSets = [set() for _ in range(9)]
        columnSets = [set() for _ in range(9)]
        boxSets = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                
                if board[i][j] in rowSets[i]:
                    return False
                rowSets[i].add(board[i][j])
                
                if board[i][j] in columnSets[j]:
                    return False
                columnSets[j].add(board[i][j])
                
                if board[i][j] in boxSets[(i // 3) * 3 + (j // 3)]:
                    return False
                boxSets[(i // 3) * 3 + (j // 3)].add(board[i][j])
            
        return True
            