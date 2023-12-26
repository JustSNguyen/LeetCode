class Solution:
    def isHappy(self, n: int) -> bool:
        processed = set()

        cur = n
        while cur != 1:
            if cur in processed:
                return False

            processed.add(cur)

            new_cur = 0

            while cur:
                digit = cur % 10
                new_cur += digit * digit
                cur //= 10

            cur = new_cur

        return True

if __name__ == '__main__':
    n = 19
    sol = Solution()
    result = sol.isHappy(n)
    print(result)