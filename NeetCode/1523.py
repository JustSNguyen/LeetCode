class Solution:
    def countOdds(self, low: int, high: int) -> int:
        new_low = low if low % 2 == 1 else low + 1
        new_high = high if high % 2 == 1 else high - 1
        return (new_high - new_low) // 2 + 1
