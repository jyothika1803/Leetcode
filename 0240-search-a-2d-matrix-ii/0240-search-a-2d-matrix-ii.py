class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i=len(matrix)-1
        j=0
        while i>=0 and j<len(matrix[0]):
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]>target:
                i-=1
            else:
                j+=1
        return False


        