"""
BackTracking 
Each step we can either add myself, or move on to other number
once we reached curr_sum > target: return 
if curr_sum == target: add it to set 
recurse to include myself, or move to next one. 
prune curr_sum - curr_num

!! important 
when designing dfs or recursion make sure to 
1. set basecase. when recursion reaches the end 
2. what to return. what do we return in deeper callstack to upper. 
3. params. 
"""
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = [] 
        nums.sort()

        def backtrack(i, path, curr_sum): 
            if curr_sum == target: 
                result.append(path[:])
                return 
            # if curr_sum > target:
            #     return
            
            for j in range(i, len(nums)): 
                if curr_sum + nums[j] <= target: 
                    path.append(nums[j])
                    backtrack(j, path, curr_sum + nums[j])
                    path.pop()
                else: break

        backtrack(0, [], 0)
        return result

                 



        