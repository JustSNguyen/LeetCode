from typing import List

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        N = len(dist)
        time = [dist[i] / speed[i] for i in range(N)]
        time = list(sorted(time))
        next_charge = 0
        count = 0
        while count < N:
            if time[count] > next_charge:
                count += 1
            else:
                break

            next_charge += 1
        return count

if __name__ == '__main__':
    sol = Solution()
    dist = [4,3,4]
    speed = [1,1,2]
    result = sol.eliminateMaximum(dist, speed)
    print(result)