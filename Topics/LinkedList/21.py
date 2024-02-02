# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        prev = None
        new_head = None
        while cur1 or cur2:
            chosen = None
            if not cur2:
                chosen = cur1
                cur1 = cur1.next
            elif not cur1:
                chosen = cur2
                cur2 = cur2.next
            elif cur1.val < cur2.val:
                chosen = cur1
                cur1 = cur1.next
            else:
                chosen = cur2
                cur2 = cur2.next

            if prev:
                prev.next = chosen
            if not new_head:
                new_head = chosen

            prev = chosen

        return new_head
