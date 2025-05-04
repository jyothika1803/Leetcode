class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        maxScore = 0
        score = 0
        i = 0
        j = len(tokens) - 1
        while i <= j:
            if tokens[i] <= power:
                score += 1
                power = power - tokens[i]
                maxScore=max(maxScore,score)
                i += 1
            elif score > 0:
                power = tokens[j] + power
                score -= 1
                j -= 1
            else:
                break
        return maxScore
        