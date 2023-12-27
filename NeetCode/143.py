# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        mid = slow
        while slow:
            next_slow = slow.next
            slow.next = prev
            prev = slow
            slow = next_slow

        cur1 = head
        cur2 = prev
        while cur2 != mid:
            next_cur_1 = cur1.next
            next_cur_2 = cur2.next

            cur1.next = cur2
            cur2.next = next_cur_1

            cur1 = next_cur_1
            cur2 = next_cur_2

        return head


if __name__ == "__main__":
    sol = Solution()
    one = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)
    five = ListNode(5)
    six = ListNode(6)

    one.next = two
    two.next = three
    three.next = None
    four.next = five
    five.next = six

    result = sol.reorderList(one)

    while result:
        print(result.val)
        result = result.next
