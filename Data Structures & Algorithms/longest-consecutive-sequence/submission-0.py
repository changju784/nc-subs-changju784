class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Numbers strictly increasing by 1 
        No contiguous 
        Nums unordered 

        Sorting O(NlogN), O(1)
        check prev num -> keep increment consecutive length -> update max length 

        Hashset 
        Iterate through nums -> if num - 1 not exists in hashset -> This means the current number is starting point of consecutive -> while num-1+length in hashset -> increment lnegth and update max length
        """
        num_set = set(nums)
        max_length = 0 

        for num in num_set: 
            if num - 1 not in num_set: 
                length = 1 
                while num + length in num_set: 
                    length += 1
                max_length = max(max_length, length)
        return max_length


        