from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        hash anagram with ascii counts 
        hashmap key tuple of counts in list, val string 
        while iterating the list, check the counts of ascii (ord(c) - ord('a'))
        hash the unique counts to hashmap as a key, store the value as its string 
        return list of values. 
        '''
        anagram_hash = defaultdict(list)

        for st in strs: 
            counts = [0] * 26 
            for c in st: 
                counts[ord(c) - ord('a')] += 1 

            anagram_hash[tuple(counts)].append(st)

        return list(anagram_hash.values())