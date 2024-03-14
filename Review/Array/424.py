from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        max_character_cnt = 0
        cnt_of = defaultdict(int)

        for i, char in enumerate(s):
            cnt_of[char] += 1
            max_character_cnt = max(max_character_cnt, cnt_of[char])
            need_to_replace = max_length + 1 - max_character_cnt
            if need_to_replace <= k:
                max_length += 1
            else:
                j = i - max_length
                cnt_of[s[j]] -= 1
                max_character_cnt = max(cnt_of.values())

        return max_length

if __name__ == '__main__':
    sol = Solution()
    string = "AABABBA"
    k = 1
    result = sol.characterReplacement(string, k)
    print(result)