class Solution:
    def reverseWords(self, s: str) -> str:
        reversed_words = ["".join(reversed(word)) for word in s.split(" ")]
        return " ".join(reversed_words)

if __name__ == '__main__':
    sol = Solution()
    s = "Let's"
    print(sol.reverseWords(s))