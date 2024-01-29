from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def set_ith_bit_to_1(num, i):
            mask = 1 << i
            return num | mask

        def get_ith_bit_value(num, i):
            return (num >> i) & 1

        result = []
        def generate(temp, chosen, length):
            if length == len(nums):
                result.append(temp)
                return

            for i, num in enumerate(nums):
                is_chosen = get_ith_bit_value(chosen, i)
                if is_chosen:
                    continue

                new_chosen = set_ith_bit_to_1(chosen, i)
                new_temp = temp[:]
                new_temp.append(num)
                generate(new_temp, new_chosen, length + 1)

        generate([], 0, 0)
        return result


if __name__ == '__main__':
    sol = Solution()
    result = sol.permute([1, 2, 3])
    print(result)