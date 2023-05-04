from typing import List 

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:  
        n = len(nums) - 1 
        def get_ith_bit_value(num, i):
            if (num & (1 << (n - i))):
                return 1 

            return 0 
        
        def set_ith_bit_to_one(num, i):
            return num | (1 << (n - i))

        checked_bits = 0
        
        # The idea is that we will put the number to their corresponding index: Number 1 will go to the 1th index, 3 will go the 3rd index so if we see another number and the index that they should go to already belonged to another number (bit == 1) then that mean it is the duplicate number
        for num in nums: 
            cur_bit = get_ith_bit_value(checked_bits, num)
            if cur_bit == 1:
                return num 
            
            checked_bits = set_ith_bit_to_one(checked_bits, num)

        

if __name__ == '__main__':
    sol = Solution()
    nums = [3,1,3,4,2]
    print(sol.findDuplicate(nums))
