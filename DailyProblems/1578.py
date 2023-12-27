from typing import List

class Solution:
    def minCost(self, colors: str, needed_time: List[int]) -> int:
        max_cost_so_far = 0
        sum_so_far = 0
        result = 0

        prev_color = None
        for i in range(len(colors)):
            color = colors[i]

            if color == prev_color:
                sum_so_far += needed_time[i]
                max_cost_so_far = max(max_cost_so_far, needed_time[i])
            else:
                result += (sum_so_far - max_cost_so_far)
                sum_so_far = needed_time[i]
                max_cost_so_far = needed_time[i]

            prev_color = color

        result += (sum_so_far - max_cost_so_far)

        return result

if __name__ == '__main__':
    sol = Solution()
    colors = "abcdaa"
    neededTime = [1, 2, 3, 4, 5, 6]
    result = sol.minCost(colors, neededTime)
    print(result)