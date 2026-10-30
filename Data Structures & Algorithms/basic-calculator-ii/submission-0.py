"""
1. valid operations? 
2. could number be long? how long? 
3. negatives? 
4. leading zeros? 
5. multiple white spaces? 
6. parantheses? 

Key Points 
1. Parsing and Execution 
1. Getting numbers
    "3213213" pointer piles up, store in extra var, type cast 
    two pointers, move right until reach non number slice [r:l] and type cast
    while reading nums, convert it to num (ord(c) - ord('0')), multiplying 10 to prev and plus curr
2. Getting operators 
    '*' and '/' should happening in advance 

3. Skipping whitespaces 

stack 
whenever facing with number get number 
whenever facing with '+' or '-' put number and ops to stack 
whenever facing with '*' pr '/' pop stack and calculate  

when num push to stack 
when ops pop 
"3+2*2"
stack = [3, +] 
curr_num = 2
curr_sum = 4

in stack, we store numbers only, when face with negative we just negate the currnum
later on we can just return sum(stack)
"""

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr_num, curr_sum = 0, 0
        curr_op = '+' 

        for i, c in enumerate(s): 
            if c.isdigit(): 
                curr_num *= 10
                curr_num += int(c)
            if c in ['+', '-', '*', '/'] or i == len(s)-1: 
                if curr_op == '+':
                    stack.append(curr_num)
                elif curr_op == '-':
                    stack.append(curr_num * -1)
                elif curr_op == '*':
                    prev_num = stack.pop()
                    stack.append(curr_num * prev_num)
                else:
                    prev_num = stack.pop()
                    stack.append(int(prev_num / curr_num))
                curr_op = c
                curr_num = 0
        
        return sum(stack)
        # while stack: 
        #     latest = stack.pop() 
        #     if latest.isnum():



