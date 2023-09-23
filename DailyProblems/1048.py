from typing import List
from functools import lru_cache

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        sorted_words = list(sorted(words, key=lambda word: len(word)))
        words_length = len(words)
        @lru_cache(maxsize=words_length)
        def get_longest_string_chain_length_from(index: int) -> int:
            if index == words_length - 1:
                return 1

            max_result = 1
            for next_index in range(index + 1, words_length):
                if is_predecessor(sorted_words[index], sorted_words[next_index]):
                    max_result = max(max_result, 1 + get_longest_string_chain_length_from(next_index))

            return max_result

        def is_predecessor(child_string: str, parent_string: str) -> bool:
            if len(child_string) != len(parent_string) - 1:
                return False

            return is_subsequence(child_string, parent_string)

        def is_subsequence(child_string: str, parent_string: str) -> bool:
            cur_child_string_char_index = 0
            for char in parent_string:
                if char == child_string[cur_child_string_char_index]:
                    cur_child_string_char_index += 1
                if cur_child_string_char_index == len(child_string):
                    return True

            return False

        max_string_chain_length: int = 0
        for i in range(words_length):
            max_string_chain_length = max(max_string_chain_length, get_longest_string_chain_length_from(i))

        return max_string_chain_length

if __name__ == '__main__':
    sol = Solution()
    words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
    result = sol.longestStrChain(words)
    print(result)