"""
inputs: asteroids integer list with two dir (pos - right, neg - left)
output: result after collision 

1. after collision bigger size remains same. 
2. empty or single asteroid happens nothing. 

t=0 [2,4,-4,-1]
t=1 [2,-1]
t=2 [2]

[4, 3, -5] -> [] -5 -> [-5]
[7, 3, -5] -> [7] -5

Stack 
while iterating through the asteroid list,
    while stack exists, and latest element in stack is pos, and current asteroid < 0:
        mutate asteroid 
        abs(latest element in stack) == abs(current negative asteroid):
            asteroid = 0 
            stack.append(asteorid)
        abs(latest element in stack) > abs(current negative asteroid):
            asteroid = 0
        abs(latest element in stack) < abs(current negative asteroid):
            stack.append(asteroid)
    
    stack.append(asteroid)

"""
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids: 
            while stack and stack[-1] > 0 and asteroid < 0:
                latest = abs(stack[-1])
                curr = abs(asteroid)
                if latest == curr: 
                    asteroid = 0 
                    stack.pop() 
                elif latest > curr: 
                    asteroid = 0 
                else: 
                    stack.pop()
            if asteroid != 0:
                stack.append(asteroid)
        return stack 