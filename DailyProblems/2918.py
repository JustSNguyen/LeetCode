from typing import List

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        minimum_sum_if_replaced_nums1 = 0
        minimum_sum_if_replaced_nums2 = 0
        number_of_zeros_in_nums1 = 0
        number_of_zeros_in_nums2 = 0

        for num in nums1:
            if num == 0:
                minimum_sum_if_replaced_nums1 += 1
                number_of_zeros_in_nums1 += 1
            else:
                minimum_sum_if_replaced_nums1 += num

        for num in nums2:
            if num == 0:
                minimum_sum_if_replaced_nums2 += 1
                number_of_zeros_in_nums2 += 1
            else:
                minimum_sum_if_replaced_nums2 += num

        new_sum = max(minimum_sum_if_replaced_nums1, minimum_sum_if_replaced_nums2)

        if new_sum > minimum_sum_if_replaced_nums1 and number_of_zeros_in_nums1 == 0:
            return -1

        if new_sum > minimum_sum_if_replaced_nums2 and number_of_zeros_in_nums2 == 0:
            return -1

        return new_sum
