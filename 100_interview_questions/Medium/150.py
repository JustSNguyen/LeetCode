from typing import List 

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        for token in tokens:
            if token != "+" and token != "-" and token != "*" and token != "/":
                num_stack.append(int(token))
            
            else:
                num2 = num_stack.pop()
                num1 = num_stack.pop()

                result = 0 
                if token == "+":
                    result = num1 + num2 
                
                if token == "-":
                    result = num1 - num2 
                
                if token == "*":
                    result = num1 * num2 
                
                if token == "/":
                    result = abs(num1) // abs(num2) 
                    if num1 * num2 < 0: 
                        result = -result
                
                num_stack.append(result)
                
        return num_stack[0] 

if __name__ == "__main__":
    sol = Solution()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    result = sol.evalRPN(tokens)
