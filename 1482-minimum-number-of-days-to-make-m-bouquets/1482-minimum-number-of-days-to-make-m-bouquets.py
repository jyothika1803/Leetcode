class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        val = m * k
        n = len(bloomDay)
        if val > n:
            return -1
        min_val = min(bloomDay)
        max_val = max(bloomDay)
        while min_val <= max_val:
            mid = (min_val + max_val) // 2
            if self.possible(bloomDay, mid, m, k):
                max_val = mid - 1
            else:
                min_val = mid + 1

        return min_val

    def possible(self, bloomDay, mid, m, k):
        n = len(bloomDay)
        cnt = 0
        noOfB = 0
        for i in range(n):
            if bloomDay[i] <= mid:
                cnt += 1
            else:
                noOfB += cnt // k
                cnt = 0

        noOfB += cnt // k
        return noOfB >= m
     