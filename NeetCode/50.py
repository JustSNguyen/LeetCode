class Solution:
    def myPow(self, x: float, n: int) -> float:
        def binary_lift_pow(cur):
            if cur == 0:
                return 1

            if cur % 2 == 0:
                val = binary_lift_pow(cur // 2)
                return val * val

            val = binary_lift_pow(cur // 2)
            return val * val * x

        if n >= 0:
            return binary_lift_pow(n)

        return 1 / binary_lift_pow(-n)

if __name__ == '__main__':
    sol = Solution()
    x = -5
    n = -3
    result = sol.myPow(x, n)
    print(result)