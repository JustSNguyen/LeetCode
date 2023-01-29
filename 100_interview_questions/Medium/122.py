from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        NEG_INF = -10**9
        number_of_days = len(prices)
        max_profit_dp_result = [[NEG_INF for _ in range(2)] for _ in range(number_of_days + 1)]
        def max_profit_dp(day_index, is_holding):
            if max_profit_dp_result[day_index][is_holding] != NEG_INF:
                return max_profit_dp_result[day_index][is_holding]
            
            if day_index == number_of_days:
                max_profit_dp_result[day_index][is_holding] = 0 
                return max_profit_dp_result[day_index][is_holding]
            
            if is_holding:
                sold_option_result = max_profit_dp(day_index + 1, 0)  + prices[day_index] 
                hold_option_result = max_profit_dp(day_index + 1, 1) 
                max_profit_dp_result[day_index][is_holding] = max(sold_option_result, hold_option_result) 
            
            else: 
                buy_option_result = max_profit_dp(day_index + 1, 1)  - prices[day_index] 
                not_buying_option_result = max_profit_dp(day_index + 1, 0) 
                max_profit_dp_result[day_index][is_holding] = max(buy_option_result, not_buying_option_result)
            
            return max_profit_dp_result[day_index][is_holding]
        
        return max_profit_dp(0, 0)
    
if __name__ == '__main__':
    sol = Solution()
    prices = [5]
    result = sol.maxProfit(prices)
    print(result)