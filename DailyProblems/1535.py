from typing import List

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        N = len(arr)
        max_arr = max(arr)

        if k >= N - 1:
            return max_arr

        winner = arr[0]
        index = 1
        consecutive_rounds_win = 0

        while winner != max_arr and consecutive_rounds_win != k:
            num = arr[index]
            if num > winner:
                winner = num
                consecutive_rounds_win = 1
            else:
                consecutive_rounds_win += 1

            index += 1

        return winner


