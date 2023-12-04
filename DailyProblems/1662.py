from typing import List 

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1_word_index = 0 
        word2_word_index = 0 

        word1_char_index = 0 
        word2_char_index = 0 


        while word1_word_index < len(word1) and word2_word_index < len(word2):
            if word1_char_index == len(word1[word1_word_index]):
                word1_word_index += 1 
                word1_char_index = 0 
            
            if word2_char_index == len(word2[word2_word_index]):
                word2_word_index += 1 
                word2_char_index = 0 
            
            if word1_word_index == len(word1) or word2_word_index == len(word2):
                break 
            
            if word1[word1_word_index][word1_char_index] == word2[word2_word_index][word2_char_index]:
                word1_char_index += 1 
                word2_char_index += 1 
            else:
                return False 
        
        return word1_word_index == len(word1) and word2_word_index == len(word2)

if __name__ == '__main__':
    sol = Solution()
    word1 = ["ab", "cef"]
    word2 = ["a", "bc"]
    result = sol.arrayStringsAreEqual(word1, word2)
    print(result)
