class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_hash = {}
        result = [] 

        for st in strs: 
            sorted_st = ''.join(sorted(st))
            if sorted_st not in anagram_hash: 
                anagram_hash[sorted_st] = [st]
            else: 
                anagram_hash[sorted_st].append(st)
        return [val for val in anagram_hash.values()]