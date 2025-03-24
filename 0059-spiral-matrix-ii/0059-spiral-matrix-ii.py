class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        r1=0
        c1=0
        r2=n-1
        c2=n-1
        matrix = [[0] * n for _ in range(n)]
        i=1
        while r1<=r2 and c1<=c2:   #O(m*n)
        #O(m+n)
            for c in range(c1,c2+1):  #O(n)
                matrix[r1][c]=i
                i+=1
            for r in range(r1+1,r2+1):  #O(m)
                matrix[r][c2]=i
                i+=1
            if r1<r2 and c1<c2:
                for c in range(c2-1,c1-1,-1): #O(n)
                    matrix[r2][c]=i
                    i+=1
                for r in range(r2-1,r1,-1): #O(m)
                    matrix[r][c1]=i
                    i+=1
            r1+=1
            c1+=1
            r2-=1
            c2-=1
        return matrix

        #Time Complexity: O(m*n)*O(m+n)-->O(m*n)
        #Space Complexity: O(1)




        