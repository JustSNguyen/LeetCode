# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        values = []
        cur = head
        while cur:
            values.append(cur.val)
            cur = cur.next

        prefixes = [value for value in values]
        for i in range(1, len(values)):
            prefixes[i] = prefixes[i - 1] + values[i]

        new_head = None
        cur = None
        N = len(values)
        max_j = -1
        for i in range(N):
            if i <= max_j:
                continue

            for j in range(N):
                prefix_sum = prefixes[j]
                if i > 0:
                    prefix_sum -= prefixes[i - 1]

                if prefix_sum == 0:
                    max_j = j

            if max_j < i:
                if not new_head:
                    new_head = ListNode(values[i])
                    cur = new_head
                else:
                    cur.next = ListNode(values[i])
                    cur = cur.next

        return new_head


