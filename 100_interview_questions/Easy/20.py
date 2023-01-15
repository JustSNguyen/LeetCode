class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        corresponding_brackets = {
            ")": "(",
            "}": "{",
            "]": "["
        }
    
        for _, char in enumerate(s):
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
                continue 

            corresponding_bracket = corresponding_brackets[char]
            if len(stack) == 0 or stack[-1] != corresponding_bracket:
                return False 

            stack.pop()
        
        return len(stack) == 0 