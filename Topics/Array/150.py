from typing import List
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = set(["+", "-", "*", "/"])
        stack = []

        for token in tokens:
            if token in operations:
                second_num = stack.pop()
                first_num = stack.pop()
                new_value = 0
                if token == "+":
                    new_value = first_num + second_num
                if token == "-":
                    new_value = first_num - second_num
                if token == "*":
                    new_value = first_num * second_num
                if token == "/":
                    new_value = math.trunc(first_num / second_num)

                stack.append(new_value)
            else:
                num = int(token)
                stack.append(num)

        return stack.pop()

if __name__ == '__main__':
    sol = Solution()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    result = sol.evalRPN(tokens)
    print(result)
