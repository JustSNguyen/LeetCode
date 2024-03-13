import math
class Solution:
    def pivotInteger(self, n: int) -> int:
        S = (n * (n + 1)) / 2
        x = int(math.sqrt(S))
        return x if x * x == S else -1