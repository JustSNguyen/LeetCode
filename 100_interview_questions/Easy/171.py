class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        string_length = len(columnTitle)
        result = 0 
        for i in range(string_length - 1, -1, -1):
            cur_char = columnTitle[i]
            result += (ord(cur_char) - ord('A') + 1) * (26 ** (string_length - i - 1))

        return result 

 