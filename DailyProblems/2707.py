from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        number_of_characters = len(s)
        find_minimum_extra_characters_dp_result = [-1 for _ in range(number_of_characters)]

        def find_minimum_extra_characters_dp(start):
            if start >= number_of_characters:
                return 0

            if find_minimum_extra_characters_dp_result[start] != -1:
                return find_minimum_extra_characters_dp_result[start]

            min_result = 1 + find_minimum_extra_characters_dp(start + 1)
            for i in range(start, number_of_characters):
                cur_substring = s[start:i + 1]
                if cur_substring in dictionary:
                    min_result = min(min_result, find_minimum_extra_characters_dp(i + 1))

            find_minimum_extra_characters_dp_result[start] = min_result

            return find_minimum_extra_characters_dp_result[start]

        return find_minimum_extra_characters_dp(0)


if __name__ == '__main__':
    sol = Solution()
    s = "he"
    dictionary = ["hello", "world"]
    result = sol.minExtraChar(s, dictionary)
    print(result)
