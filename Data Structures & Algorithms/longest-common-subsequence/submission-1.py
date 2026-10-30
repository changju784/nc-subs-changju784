class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        DFS
        if either indices match end, return 0
        if same, include this char and recurse i + 1, j + 1 
        otherwise, try both skip i or skip j, and return maximum 


        """
        memo = {} 

        def DFS(i, j): 
            if i == len(text1) or j == len(text2): 
                return 0 
            if (i, j) in memo: 
                return memo[(i, j)]
            if text1[i] == text2[j]: 
                memo[(i, j)] = 1 + DFS(i+1, j+1)
            else: 
                memo[(i, j)] = max(DFS(i+1, j), DFS(i, j+1))
            return memo[(i, j)]
        return DFS(0, 0)

