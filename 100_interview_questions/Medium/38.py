class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        previous_result = self.countAndSay(n - 1)

        prev_char = ""
        count_chars = 0 
        result = []

        for char in previous_result:
            if char != prev_char:
                if prev_char != "":
                    string = f'{count_chars}{prev_char}'
                    result.append(string)
                
                prev_char = char 
                count_chars = 1 
            
            else:
                count_chars += 1
            
        string = f'{count_chars}{prev_char}'
        result.append(string)

        result = ''.join(result)
        return result 

if __name__ == "__main__":
    n = 6
    sol = Solution()
    result = sol.countAndSay(n)
    print(result)
        