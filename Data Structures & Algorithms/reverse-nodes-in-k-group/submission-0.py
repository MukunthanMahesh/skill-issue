# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        last = head
        while last:
            length += 1
            last = last.next
    
        runs = length // k

        dummy = ListNode(0, head)
        group_prev = dummy
        curr = head

        for _ in range(runs):
            group_start = curr
            prev = None

            run_length = k
            while run_length:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                run_length -= 1       

            group_prev.next = prev
            group_start.next = curr
            group_prev = group_start         
                
        return dummy.next




    # First, verify if the remaning length is longer than k
    # Then, keep travelling k nodes forward while reversing the list
    # We need something to track the end of the list
    # We can technically use floor division, find the length of the list in one pass and iterate over the last for that many times
