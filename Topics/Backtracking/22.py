from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def generate(temp, open, close):
            if open == close == 0:
                result.append(temp)
                return

            if open > 0:
                generate(temp + "(", open - 1, close)

            if close > open:
                generate(temp + ")", open, close - 1)

        generate("", n, n)
        return result 