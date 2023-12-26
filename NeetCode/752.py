from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = deque()
        processed = set()
        deadends = set(deadends)

        if "0000" in deadends:
            return -1

        q.append(("0000", 0))

        while q:
            cur_state, cost = q.popleft()
            if cur_state == target:
                return cost

            if cur_state in processed:
                continue

            processed.add(cur_state)

            for i in range(4):
                cur_digit = int(cur_state[i])
                next_digit = cur_digit + 1 if cur_digit < 9 else 0
                prev_digit = cur_digit - 1 if cur_digit > 0 else 9

                new_state_1 = cur_state[:i] + str(next_digit) + cur_state[i+1:]
                new_state_2 = cur_state[:i] + str(prev_digit) + cur_state[i+1:]

                if new_state_1 not in deadends and new_state_1 not in processed:
                    q.append((new_state_1, cost + 1))

                if new_state_2 not in deadends and new_state_2 not in processed:
                    q.append((new_state_2, cost + 1))

        return -1

if __name__ == '__main__':
    sol = Solution()
    deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
    target = "8888"
    result = sol.openLock(deadends, target)
    print(result)