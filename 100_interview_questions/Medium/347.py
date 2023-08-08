from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = dict()
        frequency_list = dict() # frequency_list[x] = list of numbers with a frequency of x
        nums_length = len(nums)

        for num in nums:
            if not num in frequency:
                frequency[num] = 0 

            frequency[num] += 1 
        
        for num, num_frequency in frequency.items():
            if num_frequency not in frequency_list:
                frequency_list[num_frequency] = []
            
            frequency_list[num_frequency].append(num)
        
        result = []
        result_length = 0
        for freq in range(nums_length, -1, -1):
            if not freq in frequency_list:
                continue 

            for num in frequency_list[freq]:
                result.append(num)
                result_length += 1 
                if result_length == k:
                    return result 

if __name__ == '__main__':
    sol = Solution()
    nums = [1,1,1,2,2,3]
    k = 2
    print(sol.topKFrequent(nums, k))


