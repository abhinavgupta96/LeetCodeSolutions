class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        boardSize = len(board)
        def getSquareCord(squareNumber):
            row, col = (squareNumber-1) // boardSize, (squareNumber - 1) % boardSize

            if row%2:
                col = boardSize - 1 - col
            
            return boardSize - 1 - row, col
        
        visited = set([1])
        q = deque([1])
        steps = 0

        while q : 
            for _ in range(len(q)):
                currentSquare = q.popleft()

                if currentSquare == boardSize **2:
                    return steps
                
                for nextSquare in range(currentSquare +1, min(currentSquare +7, boardSize**2 +1 )):
                    i,j = getSquareCord(nextSquare)

                    if board[i][j] !=-1 : 
                        nextSquare = board[i][j]
                    
                    if nextSquare not in visited:
                        visited.add(nextSquare)
                        q.append(nextSquare)
            steps +=1
        
        return -1

