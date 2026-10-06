class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top, bot = 0, rows -1 #initialize left and right pivot per row
        
        while top <= bot :
            pivot = (top + bot)//2
            #find the located row
            if target <  matrix[pivot][0]: 
                bot = pivot -1
            elif target > matrix[pivot][-1]: #bigger than last of row 
                top = pivot + 1
            else:
                break
        if top > bot:
            return False
        
        row = matrix[pivot]
        l,r = 0, cols - 1
        while l <= r:
            mid = (l + r)//2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
