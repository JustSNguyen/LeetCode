from typing import List

# Time complexity of permuteHelper: O(N * N!) (There are N! permutations and you need O(N) to push that permutation to the result)
# Space complexity: O(N * N!): You need an array that can store N! permutations and each of those permutations has a length of N so that will be N * N! space needed in total. 

class Solution:
    def permuteHelper(
        self, nums: List[int], taken: List[bool], permutation: List[int], permutation_list: List[List[int]]): 
        if len(permutation) == len(nums):
            permutation_list.append(list(permutation))
            return 

        for i, num in enumerate(nums):
            if taken[i]: 
                continue 


            permutation.append(num)
            taken[i] = True

            self.permuteHelper(nums, taken, permutation, permutation_list)

            permutation.pop()
            taken[i] = False 
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums_length = len(nums)
        taken = [False for _ in range(nums_length)]
        permutation = []
        permutation_list = []
        
        self.permuteHelper(nums, taken, permutation, permutation_list)

        return permutation_list

if __name__ == '__main__':
    nums = [-5, 2]
    sol = Solution()
    permutation_list = sol.permute(nums)
    print(permutation_list) 