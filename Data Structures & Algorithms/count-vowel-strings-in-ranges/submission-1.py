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

vowels = set('aeiou')
        ans = []

        for start, end in queries: 
            count = 0 
            for i in range(start, end+1):
                if words[i][0] in vowels and words[i][-1] in vowels: 
                    count += 1
            ans.append(count)
        return ans

Prefix sum 
we are counting vowels repeatedly in overlapping range 
we can store number of valid voweled word counts in prefix sum array 
ex) ["aba","bcb","ece","aa","e"]
    [0, 1, 1, 2, 3, 4]
        ^        ^
query = [1, 4]
"""
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set('aeiou')
        prefix = 0
        prefix_cnt = [0] * (len(words)+1)
        ans = [0] * len(queries)
        
        # build prefix sum 
        for i, w in enumerate(words): 
            if w[0] in vowels and w[-1] in vowels: 
                prefix += 1
            prefix_cnt[i+1] = prefix 
        

        for i, q in enumerate(queries): 
            l, r = q 
            ans[i] = prefix_cnt[r+1] - prefix_cnt[l]

            
        return ans
        


        