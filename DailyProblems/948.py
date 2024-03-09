from typing import List 

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        max_score = 0 
        score = 0 
        tokens.sort()
        min_index = 0 
        max_index = len(tokens) - 1
        number_of_tokens_used = 0 

        while number_of_tokens_used != len(tokens):
            if power >= tokens[min_index]:
                score += 1 
                max_score = max(max_score, score)
                power -= tokens[min_index]
                number_of_tokens_used += 1 
                min_index += 1 
            elif score > 0:
                score -= 1 
                power += tokens[max_index]
                number_of_tokens_used += 1 
                max_index -= 1 
            else:
                return max_score
        
        return max_score
    
if __name__ == '__main__':
    sol = Solution()
    tokens = [200,100]
    power = 150
    score = sol.bagOfTokensScore(tokens, power)
    print(score)