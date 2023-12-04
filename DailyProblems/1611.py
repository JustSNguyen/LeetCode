class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0

        bits = []
        while n:
            bits.append(n % 2)
            n //= 2

        bits = list(reversed(bits))

        expected = 0
        result = 0
        N = len(bits)
        M = N
        for i in range(N):
            if bits[i] == expected:
                expected = 0
                M -= 1
                continue

            result += 2 ** (M - 1)
            expected = 1
            M -= 1

        return result


if __name__ == '__main__':
    sol = Solution()
    n = 27
    result = sol.minimumOneBitOperations(n)
    print(result)
