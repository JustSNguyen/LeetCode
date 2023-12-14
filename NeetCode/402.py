class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        removed_nums = 0
        new_num_digits = []
        for i in range(len(num)):
            if removed_nums < k and (i < len(num) - 1 and int(num[i]) > int(num[i + 1])):
                removed_nums += 1
                while removed_nums < k and new_num_digits and int(new_num_digits[-1]) > int(num[i + 1]):
                    removed_nums += 1
                    new_num_digits.pop()

            elif num[i] != "0" or len(new_num_digits) > 0:
                new_num_digits.append(num[i])

        new_num_digits = new_num_digits[:len(new_num_digits) - (k - removed_nums)]

        if not new_num_digits:
            return "0"

        return "".join(new_num_digits)

if __name__ == '__main__':
    sol = Solution()
    num = "1234567890"
    k = 9
    result = sol.removeKdigits(num, k)
    print(result)


