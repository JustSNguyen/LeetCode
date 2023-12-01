from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        target_index = 0
        for i in range(1, n + 1):
            if target_index == len(target):
                break

            if i == target[target_index]:
                operations.append("Push")
                target_index += 1
            else:
                operations.extend(["Push", "Pop"])

        return operations


if __name__ == '__main__':
    sol = Solution()
    target = [5]
    n = 5
    result = sol.buildArray(target, n)
    print(result)

