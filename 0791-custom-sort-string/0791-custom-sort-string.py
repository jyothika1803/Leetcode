class Solution:
    def customSortString(self, order: str, s: str) -> str:
        arr=[0]*26
        for char in s:
            arr[ord(char)-ord('a')]+=1
        result=[]
        for char in order:
            result.append(char*arr[ord(char)-ord('a')])
            arr[ord(char)-ord('a')]=0
        for i in range(len(arr)):
            if arr[i]>0:
                result.append(chr(i+ord('a'))*arr[i])
        return "".join(result)
