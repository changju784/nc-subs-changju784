# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
how many temps do I need to reverse two linked list nodes? 
1 -> 2 -> 3
prev = none 
temp_next = curr.next
curr.next = prev 
prev = curr 
curr = curr.next

"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head 
        prev = None
        while curr: 
            # curr 2
            temp_next = curr.next # temp_next = 3
            curr.next = prev # curr.next = 1
            prev = curr # store prev as curr prev = 2
            curr = temp_next # move current pointer to next 3
        return prev


        