from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        def is_valid(count_char):
            return count_char["a"] > 0 and count_char["b"] > 0 and count_char["c"] > 0

        j = 0 
        count_char = defaultdict(int)
        count = 0 

        for i in range(len(s)):
            count_char[s[i]] += 1
            while is_valid(count_char):
                count_char[s[j]] -= 1 
                
                if not is_valid(count_char):
                    count_char[s[j]] += 1 
                    break
                
                j += 1 

            if is_valid(count_char):
                count += (j + 1)
        
        return count 

if __name__ == '__main__':
    sol = Solution()
    s = "aaacb"
    result = sol.numberOfSubstrings(s)
    print(result)