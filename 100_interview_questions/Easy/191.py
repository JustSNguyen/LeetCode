class Solution:
    def hammingWeight(self, n: int) -> int:
        one_bit_count = 0
        while n != 0:
            bit = n % 2 
            one_bit_count += bit 
            n = n // 2 
        
        return one_bit_count

if __name__ == "__main__":
    sol = Solution()
    result = sol.hammingWeight(15)
    print(result)
