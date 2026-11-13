# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        rev_head = None
        curr = head
        n = 0

        while curr:
            new_node = ListNode(curr.val)
            new_node.next = rev_head
            rev_head = new_node
            curr = curr.next
            n += 1

        dummy = ListNode()
        dum_head = dummy
        left = head
        
        for _ in range(n // 2):
            dummy.next = ListNode(left.val)
            dummy = dummy.next
            dummy.next = ListNode(rev_head.val)
            dummy = dummy.next
            left = left.next
            rev_head = rev_head.next
        
        if n % 2 == 1:
            dummy.next = ListNode(left.val)

        new = dum_head.next
        curr = head
        while curr:
            curr.val = new.val
            curr = curr.next
            new = new.next
    

        
            



        
