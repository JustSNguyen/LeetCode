class Solution:
    def numSquares(self, n: int) -> int:
        all_squares_up_to_n = []
        cur_num = 1 
        while cur_num * cur_num <= n:
            all_squares_up_to_n.append(cur_num * cur_num)
            cur_num += 1 
        
        dp_num_squares_result = [[-1 for _ in range(len(all_squares_up_to_n))] for _ in range(n + 1)]
        def dp_num_squares(cur_num, cur_squares_index):
            if cur_num == 0: 
                dp_num_squares_result[cur_num][cur_squares_index] = 0 
                return 0 

            if dp_num_squares_result[cur_num][cur_squares_index] != -1:
                return dp_num_squares_result[cur_num][cur_squares_index]
            
            cur_square = all_squares_up_to_n[cur_squares_index]
            if cur_square > cur_num:
                dp_num_squares_result[cur_num][cur_squares_index] = dp_num_squares(cur_num, cur_squares_index - 1)
            
            elif cur_square == 1:
                dp_num_squares_result[cur_num][cur_squares_index] = cur_num
            
            else:
                dp_num_squares_result[cur_num][cur_squares_index] = min(dp_num_squares(cur_num - cur_square, cur_squares_index) + 1, dp_num_squares(cur_num, cur_squares_index - 1))

            return dp_num_squares_result[cur_num][cur_squares_index]
        
        return dp_num_squares(n, len(all_squares_up_to_n) - 1)
    
if __name__ == "__main__":
    sol = Solution()
    n = 1
    print(sol.numSquares(n))