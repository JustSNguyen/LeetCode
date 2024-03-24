from typing import List 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lf = 0 
        rg = len(nums) - 1 

        while lf < rg:
            mid = (lf + rg) // 2 

            if nums[mid] == target:
                return mid 
            
            if nums[mid] > target:
                if target >= nums[0]:
                    rg = mid - 1
                else:
                    if nums[mid] >= nums[0]:
                        lf = mid + 1 
                    else:
                        rg = mid - 1 
            
            else:
                if target < nums[0]:
                    lf = mid + 1 
                else:
                    if nums[mid] >= nums[0]:
                        lf = mid + 1 
                    else:
                        rg = mid - 1 
        
        if nums[lf] == target:
            return lf 

        return -1 
    
if __name__ == '__main__':
    sol = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 0 
    output = sol.search(nums, target)
    print(output)