class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        minimum=0
        maximum=len(arr)-1
        while minimum<maximum:
            mid=(maximum+minimum)//2

            if arr[mid]>arr[mid+1]:
                maximum=mid
            else:
                minimum=mid+1
        return minimum       