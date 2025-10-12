class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minimum=0
        maximum=len(arr)-k
        while minimum<maximum:
            mid=(minimum+maximum)//2
            if x-arr[mid]>arr[mid+k]-x:
                minimum=mid+1
            else:
                maximum=mid
        return arr[minimum:minimum+k]