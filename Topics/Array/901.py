class StockSpanner:

    def __init__(self):
        self.decreasing_stack = []
        self.prices = []


    def next(self, price: int) -> int:
        today = len(self.prices)
        while self.decreasing_stack and self.prices[self.decreasing_stack[-1]] <= price:
            self.decreasing_stack.pop()

        first_day_with_price_larger = self.decreasing_stack[-1] if self.decreasing_stack else -1
        result = today - first_day_with_price_larger

        self.decreasing_stack.append(len(self.prices))
        self.prices.append(price)

        return result


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)