from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate_all_parenthesis(total_open_brackets, total_close_brackets):
            # Generate all parenthesis, including invalid one.
            if total_open_brackets == 0 and total_close_brackets == 0:
                return [""]
            
            result = []
            if total_open_brackets > 0:
                parenthesis = generate_all_parenthesis(total_open_brackets - 1, total_close_brackets)
                for parenthese in parenthesis:
                    new_parenthesis = "(" + parenthese
                    result.append(new_parenthesis)
            
            if total_close_brackets > 0:
                parenthesis = generate_all_parenthesis(total_open_brackets, total_close_brackets - 1)
                for parenthese in parenthesis:
                    new_parenthesis = ")" + parenthese
                    result.append(new_parenthesis)

            return result 

        def validate_parenthesis(parenthesis):
            stack = []
            for bracket in parenthesis:
                if bracket == ")":
                    if not stack:
                        return False 

                    stack.pop()
                    continue 

                stack.append("(")
            
            return True 

        parentheses = list(filter(validate_parenthesis, generate_all_parenthesis(n, n)))
        return parentheses




if __name__ == '__main__':
    sol = Solution()
    expected_result = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
    my_result = sol.generateParenthesis(4)
    
    for result in expected_result:
        if result not in my_result:
            print(result)

            
        