from typing import List 

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        min_length = len(nums) + 1 

        i = 0 
        cur_sum = 0 
        for j in range(len(nums)):
            cur_sum += nums[j]
            
            while cur_sum >= k and i != j:
                cur_sum -= nums[i]
                print(cur_sum)
                if cur_sum < k: 
                    cur_sum += nums[i]
                    break 
                i += 1 
            
            print(j, cur_sum)
            
            if cur_sum >= k:
                print(j, j - i + 1)
                min_length = min(min_length, j - i + 1)
        
        if min_length == len(nums) + 1:
            return -1
        
        return min_length

if __name__ == '__main__':
    sol = Solution()
    test = [84,-37,32,40,95]
    k = 167 
    result = sol.shortestSubarray(test, k)
    print(result)