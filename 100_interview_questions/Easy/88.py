from typing import List 

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        original_nums1 = nums1[:]
        i, j, cur_result_length = 0, 0, 0

        while i < m or j < n: 
            if i == m: 
                nums1[cur_result_length] = nums2[j]
                j += 1
            
            elif j == n: 
                nums1[cur_result_length] = original_nums1[i]
                i += 1 
            
            elif original_nums1[i] < nums2[j]:
                nums1[cur_result_length] = original_nums1[i]
                i += 1 
            
            else: 
                nums1[cur_result_length] = nums2[j]
                j += 1 
            
            cur_result_length += 1 

if __name__ == '__main__':
    sol = Solution()
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1

    sol.merge(nums1, m, nums2, n)
