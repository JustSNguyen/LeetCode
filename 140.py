from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        sentences_dict = dict()
        def generate_sentences(s):
            if s in sentences_dict:
                return sentences_dict[s]
            
            sentences_dict[s] = []
            N = len(s)
            for substring_length in range(1, N + 1):
                substring = s[:substring_length]
                if substring in wordDict:
                    if substring_length == N:
                        sentences_dict[s].append(substring)
                        continue 

                    sentences = generate_sentences(s[substring_length:])
                    for sentence in sentences:
                        new_sentence = substring + ' ' + sentence
                        sentences_dict[s].append(new_sentence)
            
            return sentences_dict[s]

        return generate_sentences(s)

if __name__ == '__main__':
    sol = Solution()
    s = "pineapplepenapple"
    wordDict = ["apple","pen","applepen","pine","pineapple"]
    print(sol.wordBreak(s, wordDict))
