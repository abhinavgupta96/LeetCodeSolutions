class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        top = 0
        bottom = ROWS - 1

        while top <=bottom :
            row = (top + bottom)//2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
        if not (top<=bottom):
            return False

        row = (top + bottom)//2
        l = 0
        r = COLS - 1
        while l<=r:
            m = (l + r)//2
            if target > matrix[row][m]:
                l = m +1
            elif target < matrix[row][m]:
                r = m-1
            else:
                return True
        return False