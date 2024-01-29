class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        squar = defaultdict(set) ##key is co-ordinate of the grid ef (0,1)

        for r in range(9):
            for c in range(9) :
                if board[r][c] != "." : 
                    if board[r][c] in row[r] or \
                    board[r][c] in col[c] or \
                    board[r][c] in squar[(r//3, c//3)] : 
                        return False
                    row[r].add(board[r][c])
                    col[c].add(board[r][c])
                    squar[(r//3, c//3)].add(board[r][c])

                else:
                    continue
        return True