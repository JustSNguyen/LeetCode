from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        is_palindrome = [[False for _ in range(N)] for _ in range(N)]

        for i in range(N):
            for j in range(i, N):
                string = s[i:j + 1]
                reversed_string = string[::-1]
                is_palindrome[i][j] = (string == reversed_string)

        result = []
        def generate(temp, i):
            if i == N:
                result.append(temp)

            for j in range(i, N):
                if is_palindrome[i][j]:
                    new_temp = temp[:]
                    new_temp.append(s[i:j+1])
                    generate(new_temp, j + 1)

        generate([], 0)
        return result

if __name__ == '__main__':
    sol = Solution()
    s = "aaa"
    result = sol.partition(s)
    print(result)
