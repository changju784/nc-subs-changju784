class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Stack 
        Iterating through temps 
        peak stack compare with curr 
        if stack[-1] < curr: 
            pop, 
            result[stack_idx] = curr_idx - stack_idx
        stack element = [temp, index]

        [30,38,30,36,35,40,28]
        stack = [[30, 0]]
        [0, 0, 0, 0, 0, 0, 0]
        """
        result = [0] * len(temperatures)
        stack = []

        for curr_idx, temp in enumerate(temperatures):
            while stack: 
                if stack[-1][0] < temp: 
                    s_temp, s_idx = stack.pop() 
                    result[s_idx] = curr_idx - s_idx 
                else: 
                    break
            stack.append([temp, curr_idx])
        return result

