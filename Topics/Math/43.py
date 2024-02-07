class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        def add(num1, num2):
            result = []
            L1 = len(num1)
            L2 = len(num2)

            i1 = 0 
            i2 = 0 
            carry = 0 
            while i1 < L1 or i2 < L2:
                digit1 = int(num1[i1]) if i1 < L1 else 0 
                digit2 = int(num2[i2]) if i2 < L2 else 0 
                new_digit = digit1 + digit2 + carry 
                result.append(str(new_digit % 10))
                if new_digit >= 10:
                    carry = 1 
                else:
                    carry = 0 
                
                i1 += 1 
                i2 += 1 
            
            if carry == 1:
                result.append("1")
            
            return result 


        L1 = len(num1)
        L2 = len(num2)
        last_sum = [] 
        number_of_zeros = 0 

        for i in range(L1 - 1, -1, -1):
            digit1 = int(num1[i])
            carry = 0 
            add_result = []

            for j in range(number_of_zeros):
                add_result.append(0)

            for j in range(L2 -1, -1, -1):
                digit2 = int(num2[j])
                new_digit = digit2 * digit1 + carry 
                add_result.append(str(new_digit % 10))
                carry = 0 
                if new_digit >= 10:
                    carry = new_digit // 10 
            
            if carry > 0:
                add_result.append(str(carry))
            
            last_sum = add(last_sum, add_result)

            number_of_zeros += 1 

        result = []
        for i in range(len(last_sum) - 1 , -1, -1):
            digit = last_sum[i]
            if not result and digit == "0":
                continue 

            result.append(digit)

        return "".join(result)

if __name__ == '__main__':
    sol = Solution()
    num1 = "123"
    num2 = "456"
    result = sol.multiply(num1, num2)
    print(result)