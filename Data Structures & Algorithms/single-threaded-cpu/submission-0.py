"""
Input: tasks [enque time, duration]
output: order of task taken in CPU 

we want earlier enque time 
we want shorter processing time
if same conditions, earliest index 

Heap/Priority Queue 
enquetime, processing time, index 

Iterate through the tasks 
    Push to minheap with three factors 

While queue 
    Pop the factor and push the index to array 
"""
import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Pair each task with its original index and sort by enqueue_time
        indexed_tasks = sorted(
            (enqueue, duration, idx) for idx, (enqueue, duration) in enumerate(tasks)
        )

        avail_heap = []  # (processing_time, original_index) for arrived tasks
        result = []
        time = 0
        i = 0
        n = len(indexed_tasks)

        while i < n or avail_heap:
            # If nothing is ready yet, fast-forward time to the next task's arrival
            if not avail_heap and time < indexed_tasks[i][0]:
                time = indexed_tasks[i][0]

            # Push all tasks that have arrived by `time`
            while i < n and indexed_tasks[i][0] <= time:
                _, duration, idx = indexed_tasks[i]
                heapq.heappush(avail_heap, (duration, idx))
                i += 1

            # Pick the shortest job (tie-broken by smallest original index)
            duration, idx = heapq.heappop(avail_heap)
            result.append(idx)
            time += duration

        return result

        