"""
1. prefix, so index matters 
2. 


["bat","bag","bank","band", "bxx"]
bat 

Brute Force 
Iterate through chars at first string in the list 
For each string in the list, we check the current char exists
if we face when the two strings on i are different, 
or i reaches the end of string, 
that substring will becoem longest common prefix. 

"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_string = strs[0]
        for i in range(len(first_string)):
            for s in strs: 
                if i == len(s) or s[i] != first_string[i]:
                    return s[:i]
        return first_string
