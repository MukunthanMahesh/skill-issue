# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        l = 0
        while curr:
            curr = curr.next
            l += 1
        
        curr = temp1 = temp2 = head
        stop = l - n

        if stop == 0:
            return head.next
            
        while stop > 0:
            temp1 = curr
            curr = curr.next
            temp2 = curr.next
            stop -=1
        
        temp1.next = temp2
        return head

        
