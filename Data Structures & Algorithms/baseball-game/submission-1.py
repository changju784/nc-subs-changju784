"""
["1","2","+","C","5","D"]
[1, 2, 5, 10] -> 18

Stack O(N) O(N)
if number push to stack 
else 
    if + -> peak last two elements sum up -> push 
    elif C -> pop 
    else -> peak last element double -> push
return sum(stack)
"""
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = [] 
        for op in operations: 
            if op == '+':
                    stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                stack.append(stack[-1] * 2)
            elif op == 'C':
                stack.pop() 
            else: 
                stack.append(int(op))                
        return sum(stack)
            
        