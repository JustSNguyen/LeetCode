from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)

        existed_nums = set()

        for num in nums:
            existed_nums.add(num)

        cur_num = "0" * n

        while cur_num in existed_nums:
            print(cur_num)
            new_cur_num = []

            remember = 1

            for i in range(n - 1, -1, -1):
                new_digit = int(cur_num[i]) + remember
                if new_digit > 1:
                    new_digit %= 2
                    remember = 1
                else:
                    remember = 0

                new_cur_num.append(f"{new_digit}")

            new_cur_num = list(reversed(new_cur_num))
            cur_num = ''.join(new_cur_num)

        return cur_num


if __name__ == '__main__':
    nums = ["00", "01"]
    sol = Solution()
    result = sol.findDifferentBinaryString(nums)
    print(result)
