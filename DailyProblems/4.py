from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def find_kth_smallest_number(nums1, nums2, k):
            if not nums1:
                return nums2[k]
            if not nums2:
                return nums1[k]

            mid_a = len(nums1) // 2
            mid_b = len(nums2) // 2
            if mid_a + mid_b < k:
                if nums1[mid_a] < nums2[mid_b]:
                    return find_kth_smallest_number(nums1[mid_a + 1: ], nums2, k - mid_a - 1)
                return find_kth_smallest_number(nums1, nums2[mid_b + 1: ], k - mid_b - 1)

            elif nums1[mid_a] > nums2[mid_b]:
                return find_kth_smallest_number(nums1[:mid_a], nums2, k)
            return find_kth_smallest_number(nums1, nums2[:mid_b], k)

        nums1_length = len(nums1)
        nums2_length = len(nums2)
        if (nums1_length + nums2_length) % 2 == 1:
            return find_kth_smallest_number(nums1, nums2, (nums1_length + nums2_length) // 2)

        m1 = (nums1_length + nums2_length) // 2
        median_1 = find_kth_smallest_number(nums1, nums2, m1)
        median_2 = find_kth_smallest_number(nums1, nums2, m1 - 1)
        return (median_1 + median_2) / 2

if __name__ == '__main__':
    sol = Solution()
    nums1 = [1, 3]
    nums2 = [2]
    print(sol.findMedianSortedArrays(nums1, nums2))