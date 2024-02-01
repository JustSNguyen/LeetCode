class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        corresponding = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in s:
            if char not in corresponding:
                stack.append(char)
            else:
                if not stack or stack[-1] != corresponding[char]:
                    return False

                stack.pop()

        if stack:
            return False

        return True

