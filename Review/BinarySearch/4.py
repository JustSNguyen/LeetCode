from typing import List 

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def find_kth_smallest_number(lf1, rg1, lf2, rg2, k):
            length1 = rg1 - lf1 + 1
            length2 = rg2 - lf2 + 1 

            if length1 == 0:
                return nums2[lf2 + k - 1]
            
            if length2 == 0:
                return nums1[lf1 + k - 1]
            
            mid1 = (lf1 + rg1) // 2 
            mid2 = (lf2 + rg2) // 2 

            n1 = mid1 - lf1 + 1 
            n2 = mid2 - lf2 + 1

            if n1 + n2 > k:
                if nums1[mid1] > nums2[mid2]:
                    return find_kth_smallest_number(lf1, mid1 - 1, lf2, rg2, k)
                
                return find_kth_smallest_number(lf1, rg1, lf2, mid2 - 1, k)

            if nums1[mid1] < nums2[mid2]:
                return find_kth_smallest_number(mid1 + 1, rg1, lf2, rg2, k - n1)
            
            return find_kth_smallest_number(lf1, rg1, mid2 + 1, rg2, k - n2)
        
        m = len(nums1)
        n = len(nums2)
        total = m + n
        if total % 2 == 1:
            return find_kth_smallest_number(0, m - 1, 0, n - 1, total // 2 + 1)

        mid = total // 2
        first_median = find_kth_smallest_number(0, m - 1, 0, n - 1, mid)
        second_median = find_kth_smallest_number(0, m - 1, 0, n - 1, mid + 1)
        return (first_median + second_median) / 2
    
if __name__ == '__main__':
    sol = Solution()
    nums1 = [1, 3]
    nums2 = [2]
    result = sol.findMedianSortedArrays(nums1, nums2)
    print(result)