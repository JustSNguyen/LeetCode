class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for char in s:
            if char == "(":
                stack.append(char)
            else:
                inside_score = 0
                while stack[-1] != "(":
                    inside_score += stack.pop()

                stack.pop()

                if inside_score == 0:
                    stack.append(1)
                else:
                    stack.append(2 * inside_score)

        return sum(stack)