from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combine = [(position, speed) for position, speed in zip(position, speed)]
        combine = sorted(combine, reverse=True)

        count = 0
        prev_time = -1
        for position, speed in combine:
            distance = target - position
            time = distance / speed

            if time > prev_time:
                prev_time = time
                count += 1

        return count
