# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List, Optional
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        head = None
        prev = None
        for i, list in enumerate(lists):
            if list:
                heapq.heappush(min_heap, (list.val, i))

        while min_heap:
            min_val, index = heapq.heappop(min_heap)
            node = lists[index]
            next_node = lists[index].next
            node.next = None

            if not head:
                head = node
            else:
                prev.next = node

            prev = node

            if next_node:
                heapq.heappush(min_heap, (next_node.val, index))
                lists[index] = lists[index].next

        return head


