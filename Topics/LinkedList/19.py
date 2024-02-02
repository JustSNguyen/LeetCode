# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        N = len(nodes)

        if n == N:
            return head.next

        n_minus_1_node = nodes[N - n - 1]
        nth_node = nodes[N - n]
        n_minus_1_node.next = nth_node.next

        return head