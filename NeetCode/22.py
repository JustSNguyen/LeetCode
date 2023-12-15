from typing import List

class Solution:
    def generateParenthesis(self, n):
        parens = []
        def generate(p, open, close):
            if open:         generate(p + '(', open-1, close)
            if open < close: generate(p + ')', open, close-1)
            if open == close == 0:
                parens.append(p)

        generate('', n, n)

        return parens

if __name__ == "__main__":
    sol = Solution()
    n = 2
    result = sol.generateParenthesis(n)
    print(result)