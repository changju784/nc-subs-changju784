class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        suffix = [0] * len(arr)
        right_max = -1 

        for i in range(len(arr)-1, -1, -1):
            suffix[i] = right_max
            right_max = max(right_max, arr[i])
        return suffix