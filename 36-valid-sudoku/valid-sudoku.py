class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        This approach uses 3 hashset to check each of the condition : 
        1. row hashset is used to determine if a value in each of the row of the suduko is being repeated. 
        We use a nested for loop to iterate over each of the sudoku, the key in row hashset is the row being checked and the value is a set of the values in that row. If any duplicate is detected we exit and return False. This is how the row variable looks -> defaultdict({0: {'8', '3', '7'}...})
        2. We do the same for columns hashset, making sure there are no duplicates. This is how the col variables looks like -> defaultdict({0: {'8', '6'}, 1: {'3'}, 4: {'7'}})
        3. The third is a tricky condition where we still use a hashset but here the key is a co-ordinate value which corresponds to the position of one of the 9 mini-squares we need to check. Here is how the squar variable looks like -> defaultdict({(0, 0): {'8', '3', '6'}, (0, 1): {'1', '7'}})
        '''
        
        row = defaultdict(set)
        col = defaultdict(set)
        squar = defaultdict(set) 

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