class Solution:
    def scoreOfString(self, s: str) -> int:
        scores = []
        for c in s: 
            scores.append(ord(c) - ord('a'))
        if len(scores) == 1: 
            return scores[0]

        total_diff = 0 
        for i in range(1, len(scores)):
            total_diff += abs(scores[i-1] - scores[i])
            
        return total_diff