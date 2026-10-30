# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. 시작점을 기억하기 위한 더미(Dummy) 노드 생성
        dummy = ListNode(0)
        result = dummy
        carry = 0 

        # l1, l2가 남아있거나 올림수(carry)가 남아있을 때까지 반복
        while l1 or l2 or carry: 
            l1_num = 0
            l2_num = 0 
            
            if l1: 
                l1_num = l1.val 
                l1 = l1.next
            if l2: 
                l2_num = l2.val 
                l2 = l2.next
                
            # 두 수와 올림수 더하기
            result_num = l1_num + l2_num + carry
            
            # 새로운 올림수 계산 (10 이상이면 1, 아니면 0)
            carry = result_num // 10
            
            # 현재 노드에 값 채우기 (나머지 값)
            result.next = ListNode(result_num % 10)
            
            # 결과 포인터 이동
            result = result.next

        # 맨 처음 dummy 노드의 다음 노드부터가 진짜 리턴할 결과
        return dummy.next