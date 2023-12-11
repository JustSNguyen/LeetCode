from typing import List

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        prev = arr[0]
        cnt = 0

        for val in arr:
            if val == prev:
                cnt += 1
            else:
                cnt = 1

            if cnt > len(arr) / 4:
                return val

            prev = val

        return prev


if __name__ == '__main__':
    sol = Solution()
    test = [15,15,21,21,32,32,33,33,33,34,35]
    result = sol.findSpecialInteger(test)
    print(result)