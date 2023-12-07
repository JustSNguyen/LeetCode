class Solution:
    def largestOddNumber(self, num: str) -> str:
        last_odd_index = -1
        for i, digit in enumerate(num):
            int_digit = int(digit)
            if int_digit % 2 == 1:
                last_odd_index = i

        if last_odd_index == -1:
            return ""

        return num[:last_odd_index + 1]