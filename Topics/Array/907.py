from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        increasing_stack = []
        result = [-1 for _ in range(len(arr))]
        total_result = 0
        MOD = 10**9 + 7

        for i, num in enumerate(arr):
            while increasing_stack and arr[increasing_stack[-1]] > num:
                increasing_stack.pop()

            if not increasing_stack:
                result[i] = num * (i + 1)
            else:
                j = increasing_stack[-1]
                result[i] = num * (i - j) + result[j]

            total_result += result[i]
            total_result %= MOD

            increasing_stack.append(i)

        return total_result

if __name__ == '__main__':
    sol = Solution()
    test = [3,1,2,4]
    result = sol.sumSubarrayMins(test)
    print(result)