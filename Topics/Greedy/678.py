from collections import deque

class Solution:
    def checkValidString(self, s: str) -> bool:
        open_brackets = deque()
        stars = deque()
        for i, char in enumerate(s):
            if char == "(":
                open_brackets.append(i)
            if char == "*":
                stars.append(i)
            if char == ")":
                if open_brackets:
                    open_brackets.pop()
                elif stars:
                    stars.pop()
                else:
                    return False

        while open_brackets and stars:
            i = open_brackets[0]
            while stars and i > stars[0]:
                stars.popleft()

            if stars:
                stars.popleft()
                open_brackets.popleft()

        if open_brackets:
            return False

        return True









