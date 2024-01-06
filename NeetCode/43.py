from collections import deque 

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        N1 = len(num1)
        N2 = len(num2)
        last_sum = deque()
        power_of_ten = 0 
        i = N2 - 1 

        while i >= 0:
            remember = 0 
            digit2 = int(num2[i])
            result = deque()
            for j in range(N1-1, -1,  -1):
                digit1 = int(num1[j])
                temp = digit2 * digit1 + remember 
                result_digit = temp % 10 
                remember = temp // 10 
                result.appendleft(result_digit)
            
            if remember != 0:
                result.appendleft(remember)
            
            k = 0 
            while k < power_of_ten:
                result.append(0)
                k += 1 
            
            while len(last_sum) < len(result):
                last_sum.appendleft(0)
            while len(result) < len(last_sum):
                result.appendleft(0)
            
            new_last_sum = deque()
            remember = 0 
            while result:
                digit1 = result.pop()
                digit2 = last_sum.pop()
                temp = digit1 + digit2 + remember 
                new_digit = temp % 10 
                remember = temp // 10 
                new_last_sum.appendleft(new_digit)
            
            if remember > 0:
                new_last_sum.appendleft(remember)
            
            last_sum = new_last_sum 
            power_of_ten += 1 
            i -= 1
        
        while len(last_sum) > 1 and last_sum[0] == 0:
            last_sum.popleft()
        
        result = [str(digit) for digit in last_sum]
        return "".join(result)