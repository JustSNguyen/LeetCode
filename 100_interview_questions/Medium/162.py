from typing import List 

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        NEG_INF = -10**12
        new_nums = [NEG_INF]
        new_nums += nums 
        new_nums.append(NEG_INF)

        lf = 1 
        rg = len(new_nums) - 1
        while rg - lf > 1:
            mid_index = (rg + lf) // 2 
            if new_nums[mid_index] > new_nums[mid_index - 1] and new_nums[mid_index] > new_nums[mid_index + 1]:
                return mid_index - 1
            
            elif new_nums[mid_index] < new_nums[mid_index + 1]:
                lf = mid_index + 1 
            
            else:
                rg = mid_index
        
        return lf - 1
    
if __name__ == "__main__":
    nums = [1]
    sol = Solution()
    print(sol.findPeakElement(nums))
            