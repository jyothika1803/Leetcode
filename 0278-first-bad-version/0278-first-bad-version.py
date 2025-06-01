# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        minimum=1
        maximum=n
        while minimum<maximum:
            mid=(maximum+minimum)//2
            if isBadVersion(mid):
                maximum=mid
            else:
                minimum=mid+1
        return minimum

        