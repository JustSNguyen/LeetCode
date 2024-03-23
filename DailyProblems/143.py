from typing import Optional
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return head

        tail = head
        while tail.next:
            tail = tail.next

        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            fast = fast.next
            slow = slow.next

        prev = None
        mid = slow
        while slow:
            next_slow = slow.next
            slow.next = prev
            prev = slow
            slow = next_slow

        cur1 = head
        cur2 = tail
        prev = None
        while cur1 != mid:
            next_cur_1 = cur1.next
            next_cur_2 = cur2.next if cur2 else None
            cur1.next = cur2

            if prev:
                prev.next = cur1
            if cur2:
                cur2.next = None

            cur1 = next_cur_1
            prev = cur2
            cur2 = next_cur_2