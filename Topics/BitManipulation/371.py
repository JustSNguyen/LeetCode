class Solution:
    def getSum(self, a: int, b: int) -> int:
        if abs(a) < abs(b):
            return self.getSum(b, a)

        sign = 1 if a > 0 else -1

        if a * b > 0:
            a = abs(a)
            b = abs(b)
            while b > 0:
                carry = (a & b) << 1
                a = a ^ b
                b = carry
        else:
            a = abs(a)
            b = abs(b)
            while b > 0:
                carry = (~a & b) << 1
                a = a ^ b
                b = carry

        a *= sign
        return a

if __name__ == '__main__':
    a = 0
    b = 17
    sol = Solution()
    result = sol.getSum(a, b)
    print(result)