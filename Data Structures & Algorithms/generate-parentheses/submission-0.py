"""
1. In each step we can either choose to generate ( or )
2. We need to know how many numbers of open parantheses exist 

recursion 
- params: current index, current string
- basecase: when we reach the end of string n 
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def recursion(op, cl, curr_string):
            if op + cl == 2*n: 
                if op == n and cl == n: 
                    result.append(curr_string)
                return 
            if op < n: 
                recursion(op + 1, cl, curr_string + '(')
            if cl < op: 
                recursion(op, cl + 1, curr_string + ')')
            
                
            
        recursion(1, 0, '(')
        return result
        
                



            

        