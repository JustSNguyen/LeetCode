class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_digit = -1

        prev = ""
        cur_length = 0
        for char in num:
            if char == prev:
                cur_length += 1
            else:
                cur_length = 1

            if cur_length == 3:
                digit = int(char)
                max_digit = max(max_digit, digit)

            prev = char

        if max_digit == -1:
            return ""

        return f"{max_digit}" * 3
