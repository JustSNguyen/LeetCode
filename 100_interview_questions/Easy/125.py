class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_alphabetical(char):
            return 'a' <= char <= 'z'

        def is_numeric(char):
            return '0' <= char <= '9'

        normalized_s = []

        for char in s:
            lowercase_char = char.lower()
            if not is_alphabetical(lowercase_char) and not is_numeric(lowercase_char):
                continue

            normalized_s.append(lowercase_char)

        normalized_s = ''.join(normalized_s)
        normalized_s_length = len(normalized_s)

        for i in range(normalized_s_length // 2):
            if normalized_s[i] != normalized_s[normalized_s_length - i - 1]:
                return False 
            
        return True 

if __name__ == '__main__':
    s = "0P"
    sol = Solution()
    ans = sol.isPalindrome(s)
    print(ans)

        