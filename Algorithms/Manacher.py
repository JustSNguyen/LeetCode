class Manacher:
    def __init__(self, string):
        self.string = string

    def get_longest_odd_palindromes(self):
        N = len(self.string)
        result = [0 for _ in range(N)]
        left = 0
        right = 0

        for i in range(N):
            if i > right:
                result[i] = 0
            else:
                result[i] = min(right - i, result[left + right - i])

            while i - result[i] - 1 >= 0 and i + result[i] + 1 < N and self.string[i - result[i] - 1] == self.string[
                i + result[i] + 1]:
                result[i] += 1

            if i + result[i] > right:
                right = i + result[i]
                left = i - result[i]

        return result

    def get_longest_even_palindromes(self):
        N = len(self.string)
        result = [0 for _ in range(N)]
        left = 0
        right = 0

        for i in range(N):
            j = i + 1
            if j > right:
                result[i] = 0
            else:
                result[i] = min(right - j + 1, result[left + right - j])

            while i - result[i]  >= 0 and i + result[i] + 1 < N and self.string[i - result[i]] == self.string[
                i + result[i] + 1]:
                result[i] += 1

            if i + result[i] > right:
                right = i + result[i]
                left = i - result[i] + 1

        return result


if __name__ == '__main__':
    string = "abbaabba"
    manacher = Manacher(string)
    manacher.get_longest_even_palindromes()
