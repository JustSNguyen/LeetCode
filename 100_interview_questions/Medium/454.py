from typing import List 

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        def get_sum_dictionary(arr1, arr2):
            sum_arr1_arr2 = dict()
            for num1 in arr1:
                for num2 in arr2:
                    cur_sum = num1 + num2 
                    if cur_sum not in sum_arr1_arr2:
                        sum_arr1_arr2[cur_sum] = 0 
                    
                    sum_arr1_arr2[cur_sum] += 1 

            return sum_arr1_arr2


        sum_nums1_nums2 = get_sum_dictionary(nums1, nums2)
        sum_nums3_nums4 = get_sum_dictionary(nums3, nums4)

        total_sum_count = 0 
        for possible_sum in sum_nums1_nums2:
            if -possible_sum in sum_nums3_nums4:
                total_sum_count += sum_nums1_nums2[possible_sum] * sum_nums3_nums4[-possible_sum]
        
        return total_sum_count
    
if __name__ == "__main__":
    sol = Solution()
    nums1 = [0]
    nums2 = [0]
    nums3 = [0]
    nums4 = [0]
    result = sol.fourSumCount(nums1, nums2, nums3, nums4)
    print(result)

        
        