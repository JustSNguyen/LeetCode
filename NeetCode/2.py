from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = l1
        h2 = l2
        remember = 0

        prev = None
        root = None

        while h1 or h2:
            val1 = h1.val if h1 else 0
            val2 = h2.val if h2 else 0
            new_val = val1 + val2 + remember

            if new_val >= 10:
                remember = 1
                new_val -= 10
            else:
                remember = 0

            if not root:
                root = ListNode(new_val)
            else:
                prev.next = ListNode(new_val)

            h1 = h1.next if h1 else h1
            h2 = h2.next if h2 else h2

            if not prev:
                prev = root
            else:
                prev = prev.next

        if remember == 1:
            prev.next = ListNode(remember)

        return root

if __name__ == '__main__':
    sol = Solution()

    two_1 = ListNode(2)
    four_1 = ListNode(4)
    three_1 = ListNode(3)

    two_1.next = four_1
    four_1.next = three_1

    five_2 = ListNode(5)
    six_2 = ListNode(6)
    four_2 = ListNode(4)

    five_2.next = six_2
    six_2.next = four_2

    result = sol.addTwoNumbers(two_1, five_2)

    cur = result
    while cur:
        print(cur.val)
        cur = cur.next



