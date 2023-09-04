class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def is_symmetric(number):
            digits = []
            while number > 0:
                digit = number % 10
                digits.append(digit)
                number //= 10

            if len(digits) % 2 != 0:
                return False

            last_half_sum = 0
            for i in range(len(digits) // 2):
                last_half_sum += digits[i]

            other_half_sum = sum(digits) - last_half_sum
            return other_half_sum == last_half_sum

        number_of_symmetric_integers = 0
        for num in range(low, high + 1):
            if not is_symmetric(num):
                continue

            number_of_symmetric_integers += 1

        return number_of_symmetric_integers

if __name__ == '__main__':
    sol = Solution()
    low = 1200
    high = 1200
    result = sol.countSymmetricIntegers(low, high)
    print(result)
