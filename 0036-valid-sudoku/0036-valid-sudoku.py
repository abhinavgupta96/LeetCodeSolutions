from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = True
        #condition1 - my approach
        for i in board:
            hashmap = {}
            for j in i:
                if j != ".":
                    if j not in hashmap:
                        hashmap[j]=1
                    else:
                        valid = False
                        break
    
        ##condition2 - my approach
        for i in range(9):
            hashmap= {}
            for j in range(9):
                if board[j][i]!=".":
                    if board[j][i] not in hashmap :
                        hashmap[board[j][i]]=1
                    else:
                        valid = False
                        break    
    ##condition3 - neetcode approach
        squares = defaultdict(set) ##create a dict with key as a set of co-ordinates for the smaller 3x3 squares
        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                if board[r][c] in squares[(r//3,c//3)]: ##r//3 and c//3 give us the co-ordinate of the square, if board[r][c] is not in that square we add it
                    valid = False
                    return valid
                squares[(r//3,c//3)].add(board[r][c])

        return valid
        