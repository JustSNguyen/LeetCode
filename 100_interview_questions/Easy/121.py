from typing import List 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        number_of_days = len(prices)
        max_profit_dp_result = [[-1 for _ in range(2)] for _ in range(number_of_days)]
        def max_profit_dp(day, is_holding_stock):
            if day >= number_of_days: 
                return 0 
            
            if max_profit_dp_result[day][is_holding_stock] != -1: 
                return max_profit_dp_result[day][is_holding_stock]
            
            if is_holding_stock:
                max_profit_dp_result[day][is_holding_stock] = max(
                    max_profit_dp(day + 1, is_holding_stock), 
                    prices[day]) 
            
            else: 
                max_profit_dp_result[day][is_holding_stock] = max(
                    max_profit_dp(day + 1, False), 
                    max_profit_dp(day + 1, True) - prices[day]) 
                
            return max_profit_dp_result[day][is_holding_stock]
        
        return max_profit_dp(0, False)
        
if __name__ == '__main__':
    sol = Solution()
    prices = [7,6,4,3,1]
    result = sol.maxProfit(prices)
    print(result)