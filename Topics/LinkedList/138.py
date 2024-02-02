
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


from typing import Optional
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        cur = head
        while cur:
            next_cur = cur.next
            cur.next = Node(cur.val, next_cur, None)
            cur = next_cur

        original = head
        while original:
            next_original = original.next.next
            copy = original.next
            copy.next = next_original.next if next_original else None
            copy.random = original.random.next if original.random else None
            original = next_original

        return head.next
