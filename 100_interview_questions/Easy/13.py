class Solution:
    def romanToInt(self, s: str) -> int:
        value = dict() 
        value["I"] = 1 
        value["IV"] = 4 
        value["V"] = 5 
        value["IX"] = 9 
        value["X"] = 10
        value["XL"] = 40 
        value["L"] = 50 
        value["XC"] = 90 
        value["C"] = 100 
        value["CD"] = 400 
        value["D"] = 500 
        value["CM"] = 900 
        value["M"] = 1000 

        i = 0 
        result = 0 
        while i < len(s):
            cur_char = s[i]
            if i == len(s) - 1:
                result += value[cur_char]
                break 

            next_char = s[i + 1]
            symbol = cur_char
            next_i = i + 1

            if value[next_char] > value[cur_char]:
                symbol += next_char
                next_i = i + 2 
            
            result += value[symbol]
            i = next_i 
        
        return result 

if __name__ == '__main__':
    s = "III"
    print(Solution().romanToInt(s))

