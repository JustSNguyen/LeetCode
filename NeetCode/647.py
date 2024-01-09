class Manacher:
    def __init__(self, string):
        self.string = string

    def get_longest_odd_palindromes(self):
        left = -1
        right = -1
        N = len(self.string)
        result = [0 for _ in range(N)]

        for i in range(N):
            if i > right:
                result[i] = 0
            else:
                result[i] = min(result[right - i + left], right - i)

            while i - result[i] - 1 >= 0 and i + result[i] + 1 < N and self.string[i - result[i] - 1] == self.string[
                i + result[i] + 1]:
                result[i] += 1

            if i + result[i] > right:
                right = i + result[i]
                left = i - result[i]

        return result

    def get_longest_even_palindromes(self):
        left = -1
        right = -1
        N = len(self.string)
        result = [0 for _ in range(N)]

        for i in range(N):
            j = i + 1

            if j > right:
                result[i] = 0
            else:
                result[i] = min(right - j + 1, result[left + right - j])

            while i - result[i] >= 0 and j + result[i] < N and self.string[i - result[i]] == self.string[j + result[i]]:
                result[i] += 1

            if i + result[i] > right:
                right = i + result[i]
                left = i - result[i] + 1

        return result


class Solution:
    def countSubstrings(self, s: str) -> int:
        manacher = Manacher(s)

        even_palindromes = sum(manacher.get_longest_even_palindromes())
        odd_palindromes = sum(manacher.get_longest_odd_palindromes()) + len(s)

        return even_palindromes + odd_palindromes


if __name__ == '__main__':
    s = "aaa"
    sol = Solution()
    result = sol.countSubstrings(s)
    print(result)
