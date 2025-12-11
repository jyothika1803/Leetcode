class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row=[0]*m
        col=[0]*n

        for r,c in indices:
            row[r]+=1
            col[c]+=1
        odd_count=0

        for i in range(m):
            for j in range(n):
                if (row[i]+col[j])%2==1:
                    odd_count+=1
        return odd_count
