"""
input: words list of strings, queries list of intervals 
ouput: count # words that starts&ends with vowel in interval range  

Brute Force O(len(queries) * len(words))
Iterate through queries 
    Initiate counter 
    For each query range, 
        index the corresponding words
        check if word starts/ends with vowels. 
        if so count up. 
"""
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a', 'e', 'i', 'o', 'u']
        ans = []

        for start, end in queries: 
            count = 0 
            for i in range(start, end+1):
                if words[i][0] in vowels and words[i][-1] in vowels: 
                    count += 1
            ans.append(count)
        return ans
        


        