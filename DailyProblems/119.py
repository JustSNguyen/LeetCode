from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        previous_result = [1]
        for i in range(1, rowIndex + 1):
            new_result = [1]
            for j in range(1, len(previous_result)):
                new_result.append(previous_result[j - 1] + previous_result[j])
            new_result.append(1)
            previous_result = new_result

        return previous_result
