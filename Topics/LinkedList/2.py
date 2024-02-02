# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = None
        prev = None

        while l1 or l2:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
            total = digit1 + digit2 + carry

            if total >= 10:
                carry = 1
            else:
                carry = 0

            node = ListNode(total % 10)
            if prev:
                prev.next = node
            else:
                head = node

            prev = node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry == 1:
            prev.next = ListNode(1)

        return head
