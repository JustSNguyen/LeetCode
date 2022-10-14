from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        string_length = len(s)
        for i in range(string_length // 2):
            s[i], s[string_length - i - 1] = s[string_length - i - 1], s[i]


if __name__ == '__main__':
    sol = Solution()
    s = ["2"]
    sol.reverseString(s) 
    print(s)
        