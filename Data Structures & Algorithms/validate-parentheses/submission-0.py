class Solution:
    def isValid(self, s: str) -> bool:
        """
        stack 
        """
        stack = []
        for p in s: 
            # if any open paran 
            if p in ["{", "[", "("]:
                stack.append(p)
            else: 
                if len(stack) == 0: 
                    return False 
                open_p = stack.pop()
                if open_p is "(" and p is not ")": 
                    return False 
                if open_p is "{" and p is not "}":
                    return False 
                if open_p is "[" and p is not "]": 
                    return False 
        if len(stack) > 0: 
            return False 
        return True 

