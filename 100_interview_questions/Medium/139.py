from typing import List 

class Solution:
    def wordBreak(self, s: str, word_list) -> bool:
        max_word_length = 0 
        word_dict = dict()
        for word in word_list:
            max_word_length = max(len(word), max_word_length)
            word_dict[word] = 1
        
        validate_string_is_breakable_dp_result = dict()
        def validate_string_is_breakable_dp(string):
            if string == "":
                return True

            if string in validate_string_is_breakable_dp_result:
                return validate_string_is_breakable_dp_result[string]
            
            cur_prefix = ""
            breakable = False 
            for i in range(min(len(string), max_word_length)):
                cur_prefix += string[i]
                if cur_prefix not in word_dict:
                    continue 
                
                rest_of_the_string = string[len(cur_prefix):]
             
                temp_breakable = validate_string_is_breakable_dp(rest_of_the_string)

                if temp_breakable:
                    breakable = True 
                    break 
            
            validate_string_is_breakable_dp_result[string] = breakable
            return validate_string_is_breakable_dp_result[string]

        return validate_string_is_breakable_dp(s)

if __name__ == "__main__":
    sol = Solution()
    s = "applepenapple"
    wordDict = ["apple","pen"]
    print(sol.wordBreak(s, wordDict))