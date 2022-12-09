from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = True
        #condition1
        print("Entering condition1")
        for i in board:
            hashmap = {}
            for j in i:
                if j != ".":
                    if j not in hashmap:
                        hashmap[j]=1
                    else:
                        valid = False
                        break
    
        ##condition2
        print("Entering condition2")
        for i in range(9):
            hashmap= {}
            for j in range(9):
                if board[j][i]!=".":
                    if board[j][i] not in hashmap :
                        hashmap[board[j][i]]=1
                    else:
                        valid = False
                        break    
    ##condition3
        print("Entering condition3")
        squares = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                if board[r][c] in squares[(r//3,c//3)]:
                    valid = False
                    return valid
                squares[(r//3,c//3)].add(board[r][c])
            print(squares[(r//3,c//3)])

        return valid
        