# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        curr1, curr2 = l1, l2
        carry = 0

        while curr1 or curr2 or carry:
            a = curr1.val if curr1 else 0
            b = curr2.val if curr2 else 0

            total = a + b + carry
            carry = total // 10
            tail.next = ListNode(total % 10)

            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
            tail = tail.next

        return dummy.next
