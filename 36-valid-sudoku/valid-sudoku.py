class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowDict = defaultdict(set)
        colDict = defaultdict(set)
        squareDict = defaultdict(set)

        ROWS, COL = len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COL):
                if board[r][c]==".":
                    continue
                if board[r][c] in rowDict[r] or board[r][c] in colDict[c] or board[r][c] in squareDict[(r//3,c//3)]:
                    return False
                rowDict[r].add(board[r][c]) 
                colDict[c].add(board[r][c])
                squareDict[(r//3,c//3)].add(board[r][c])
        return True