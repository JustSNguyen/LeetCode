class Solution:
    def encode(self, strings):
        new_string = []
        for string in strings:
            string_length = len(string)
            new_string.append(f"{string_length}/{string}")
        
        return "".join(new_string)
        

    def decode(self, string):
        result = []
        i = 0 
        while i < len(string):
            string_length = 0 
            while string[i] != "/":
                digit = int(string[i])
                string_length = string_length * 10 + digit 
                i += 1 
            
            i += 1 
            result_string = string[i:i + string_length]
            result.append(result_string) 

            i += string_length 
        
        return result 
    
if __name__ == '__main__':
    sol = Solution()
    strings = ["I", "just", "want", "to", "test"]

    encoded_result = sol.encode(strings)
    print(encoded_result)

    decoded_result = sol.decode(encoded_result)
    print(decoded_result)
