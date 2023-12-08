from typing import List

class Solution:
    def carFleet(self, target: int, positions: List[int], speed: List[int]) -> int:
        speed_based_on_position = dict()

        for i, position in enumerate(positions):
            if position not in speed_based_on_position:
                speed_based_on_position[position] = speed[i]
            else:
                speed_based_on_position[position] = min(speed_based_on_position[position], speed[i])

        positions = sorted(positions, reverse=True)
        takes = [((target - position) / speed_based_on_position[position]) for position in positions]

        result = 0
        prev_pos = 0
        for i in range(1, len(positions)):
            if takes[i] > takes[prev_pos]:
                result += 1
                prev_pos = i

        return result + 1

if __name__ == '__main__':
    position = [0, 2, 4]
    speed = [4, 2, 1]
    target = 100
    sol = Solution()
    result = sol.carFleet(target, position, speed)
    print(result)