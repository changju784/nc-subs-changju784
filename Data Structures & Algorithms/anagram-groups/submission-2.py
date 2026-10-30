from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_hash = defaultdict(list)

        for st in strs: 
            counts = [0] * 26 
            for c in st: 
                counts[ord(c) - ord('a')] += 1 

            anagram_hash[tuple(counts)].append(st)

        return list(anagram_hash.values())