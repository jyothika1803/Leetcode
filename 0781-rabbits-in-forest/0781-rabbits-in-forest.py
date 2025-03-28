class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        hash_map={}
        ans=0
        for answer in answers:
            if answer in hash_map:
                hash_map[answer]-=1
            else:
                hash_map[answer]=answer
                ans+=answer+1
            if hash_map[answer]==0:
                del hash_map[answer]
        return ans




