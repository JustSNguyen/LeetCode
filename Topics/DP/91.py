class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp_1 = 1 if s[n - 1] != "0" else 0 
        dp_2 = 1 

        for i in range(n - 2, -1, -1):
            if s[i] == "0":
                dp_2 = dp_1 
                dp_1 = 0 
            else:
                dp = 0 
                dp += dp_1
                if s[i] == "1" or (s[i] == "2" and s[i + 1] < "7"):
                    dp += dp_2 

                dp_2 = dp_1 
                dp_1 = dp 

        return dp_1