from typing import List
from collections import defaultdict

class Solution:
    def isNStraightHand(self, hands: List[int], group_size: int) -> bool:
        N = len(hands)

        if N % group_size != 0:
            return False

        cnt = defaultdict(int)
        for hand in hands:
            cnt[hand] += 1

        sorted_hands = list(cnt.keys())
        sorted_hands.sort()
        divided = 0
        smallest_index = 0
        while divided != N:
            smallest = sorted_hands[smallest_index]
            while cnt[sorted_hands[smallest_index]] == 0:
                smallest_index += 1
                smallest = sorted_hands[smallest_index]

            for i in range(smallest, smallest + group_size):
                if cnt[i] == 0:
                    return False

                cnt[i] -= 1
                divided += 1

        return True


