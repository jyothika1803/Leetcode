class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldier_row=[]
        for i in range(len(mat)):
            soldier_count=0
            for num in mat[i]:
                if num==1:
                    soldier_count+=1
                else:
                    break
            soldier_row.append((soldier_count,i))
        soldier_row.sort()
        result=[]
        for j in range(k):
            result.append(soldier_row[j][1])
        return result