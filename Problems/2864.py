class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s_length = len(s)
        number_of_one_bits = 0
        for bit in s:
            number_of_one_bits += (bit == "1")

        number_of_zero_bits = s_length - number_of_one_bits
        number_of_one_bits -= 1
        new_s = ["1"] + ["0"] * number_of_zero_bits + ["1"] * number_of_one_bits
        new_s = list(reversed(new_s))
        return "".join(new_s)

if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumOddBinaryNumber("1000"))


