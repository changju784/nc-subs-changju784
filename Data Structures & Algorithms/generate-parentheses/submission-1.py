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
        stack = []

        def recursion(op, cl):
            if op + cl == 2*n: 
                if op == n and cl == n: 
                    result.append("".join(stack))
                return 
            if op < n: 
                stack.append("(")
                recursion(op+1, cl)
                stack.pop()
            if cl < op: 
                stack.append(")")
                recursion(op, cl + 1)
                stack.pop()
            
                
            
        recursion(0, 0)
        return result
        
                



            

        