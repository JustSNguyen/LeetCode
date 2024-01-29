from typing import List
from collections import defaultdict

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        digit_to_chars = defaultdict(list)

        ascii = ord('a')
        for i in range(2, 10):
            options = 3
            if i == 7 or i == 9:
                options = 4

            for j in range(options):
                next_char = chr(ascii)
                digit_to_chars[str(i)].append(next_char)
                ascii += 1

        result = []
        def generate(temp, index):
            if index == len(digits):
                result.append(temp)
                return

            digit = digits[index]
            for char in digit_to_chars[digit]:
                new_temp = temp + char
                generate(new_temp, index + 1)

        generate("", 0)
        return result
if __name__ == '__main__':
    sol = Solution()
    digits = "23"
    result = sol.letterCombinations(digits)
    print(result)