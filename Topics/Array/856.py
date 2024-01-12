class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for char in s:
            if char == "(":
                stack.append(char)
            else:
                inside = 0
                while stack[-1] != "(":
                    inside += stack.pop()
                stack.pop()
                stack.append(max(1, 2 * inside))

        return sum(stack)

if __name__ == '__main__':
    sol = Solution()
    test = "((()))"
    result = sol.scoreOfParentheses(test)
    print(result)
