"""
between last two char 
and M or F is age 

Iterate reverse 

"""
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0 
        for detail in details: 
            if int(detail[11:13]) > 60:
                count += 1
        return count
        
        