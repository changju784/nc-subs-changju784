from collections import defaultdict 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        s1 = "abc", s2 = "lecabee"
        order doesn't matter 
        but charactors have to be contiguous 

        Two pointers 
        1. We store chars frequency hashmap 
        ex) {a: 1, b: 1, c: 1}
        2. Sliding window -- window size of len(s1) 
        l = 0 r = l + len(s1)
        if s2[l] is not in hash_map: 
            move both pointer to right -> slide the window
        else: 
            hash_map_compare = {} 
            while l < r: 
                hash_map_compare[l] += 1 
                if s2[l] not in hash_map: 
                    break 
                l += 1
            if hash_map_compare == hash_map: 
                return True 

            
        ex) {a: 1, b: 1, c: 1}
        ex) {a: 1, b: 1, c: 1}
        lecabee
          ^ 
        
        """
        # # 1. Store char freq map 
        # hash_map = defaultdict(int)
        # for c in s1: 
        #     hash_map[c] += 1
        # print(hash_map)
        for l in range(len(s2) - len(s1) + 1): 
            if s2[l] in s1: 
                string_to_compare = s2[l:l+len(s1)]
                if sorted(string_to_compare) == sorted(s1):
                    return True

        return False 