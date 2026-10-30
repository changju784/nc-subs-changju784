"""
use hashmap key -> list of (timestamp, value)

"""
from collections import defaultdict
class TimeMap:
    def __init__(self):
        self.hash_map = defaultdict()
    
    def set(self, key: str, value: str, timestamp: int) -> None: 
        if key not in self.hash_map:
            self.hash_map[key] = []
        self.hash_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str: 
        result = "" 
        if key not in self.hash_map: 
            return result 

        values = self.hash_map[key]
        l, r = 0, len(values)-1 
        while l <= r: 
            mid = (l + r) // 2 
            if values[mid][1] <= timestamp: 
                result = values[mid][0]
                l = mid + 1
            else: 
                r = mid - 1
        return result


        
