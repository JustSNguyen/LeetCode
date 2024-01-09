# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

import random

class Solution:
    def findSecretWord(self, words, master):
        def count_matches(word1, word2):
            count = 0
            for i in range(6):
                if word1[i] == word2[i]:
                    count += 1
            return count

        possible_solutions = words
        k = master.guess(words[0])
        guess = words[0]
        for _ in range(10):
            if k == 6: break

            new_possible_solutions = []
            for word in possible_solutions:
                if count_matches(word, guess) == k:
                    new_possible_solutions.append(word)

            possible_solutions = new_possible_solutions
            guess = random.choice(possible_solutions)
            k = master.guess(guess)

# if __name__ == '__main__':
#     sol = Solution()
#     secret_word = ""hbaczn"
