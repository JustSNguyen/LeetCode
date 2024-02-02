# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse_list_iteratively(head)

    def reverse_list_iteratively(self, head):
        prev = None
        cur = head

        while cur:
            next_cur = cur.next
            cur.next = prev
            prev = cur
            cur = next_cur

        return prev

    def reverse_list_recursively(self, head: Optional[ListNode]):
        if not head:
            return None, None

        new_tail, new_head = self.reverse_list_recursively(head.next)
        if new_tail:
            new_tail.next = head

        if not new_head:
            new_head = head

        head.next = None
        return head, new_head
