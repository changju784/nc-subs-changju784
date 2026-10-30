# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
1 -> 2 -> 3 -> 4
Two pointers 
move r pointer n steps ahead -> gap between l, r is n 
when r reaches the end, l is at index to remove 

"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        r = head  
        l = dummy
        while n > 0: 
            r = r.next
            n -= 1
        while r: 
            r = r.next
            l = l.next
        l.next = l.next.next
        
        return dummy.next

        