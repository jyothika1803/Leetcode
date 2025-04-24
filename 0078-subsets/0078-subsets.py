class Solution:
    def findAll(self, i: int, n: int, ans: List[List[int]], result: List[int], arr: List[int]):
        if i == n:
            ans.append(result[:])  # make a copy of result
            return
        # Include arr[i]
        result.append(arr[i])
        self.findAll(i + 1, n, ans, result, arr)
        result.pop()  # backtrack
        # Exclude arr[i]
        self.findAll(i + 1, n, ans, result, arr)

    def subsets(self, arr: List[int]) -> List[List[int]]:
        ans = []
        result = []
        self.findAll(0, len(arr), ans, result, arr)
        return ans


        