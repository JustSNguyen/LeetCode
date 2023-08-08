class Solution:
    def finalString(self, s: str) -> str:
        result_string_list = []
        
        for char in s: 
            if char != "i":
                result_string_list.append(char)
            
            else:
                result_string_list = list(reversed(result_string_list))
        
        return "".join(result_string_list)
    

if __name__ == "__main__":
    sol = Solution()
    test_string = "string"
    result_string = sol.finalString(test_string)
    print(result_string)
