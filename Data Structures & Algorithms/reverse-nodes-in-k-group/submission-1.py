# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        last, length = head, 0
        while last:
            length += 1
            last = last.next
        
        runs = length // k

        dummy = ListNode(0, head)
        group_prev = dummy
        curr = head

        for _ in range(runs):
            group_start, prev, run = curr, None, k
            
            while run:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                run -= 1
            
            group_prev.next = prev
            group_start.next = curr
            group_prev = group_start
        
        return dummy.next
