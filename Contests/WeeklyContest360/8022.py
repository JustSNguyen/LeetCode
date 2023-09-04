class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        cur_num = 1 
        cur_sum = 0 
        
        while n > 0:
            other_num = target - cur_num 
            while other_num < cur_num and other_num >= 1:
                cur_num += 1 
                other_num = target - cur_num 
            
            cur_sum += cur_num 
            cur_num += 1 
            n -=  1

        return cur_sum 

if __name__ == '__main__':
    sol = Solution()
    n = 3
    target = 3 
    result = sol.minimumPossibleSum(n, target)
    print(result)