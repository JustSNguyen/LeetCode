from typing import List 

class Solution:
    def findArray(self, prefs: List[int]) -> List[int]:
        previous_pref_bits = []
        result = []

        def convert_value_to_bits(value: int) -> List[int]:
            bits = []
            while value > 0:
                bit = value % 2 
                bits.append(bit)
                value //= 2 
            return bits 


        for pref in prefs:
            if not previous_pref_bits:
                result.append(pref)
                previous_pref_bits = convert_value_to_bits(pref)
            else:
                pref_bits = convert_value_to_bits(pref)
                length = max(len(pref_bits), len(previous_pref_bits))
                
                while len(pref_bits) < length:
                    pref_bits.append(0)
                while len(previous_pref_bits) < length:
                    previous_pref_bits.append(0)
                
                element = 0 
                base = 0 
                for i in range(length):
                    pref_bit = pref_bits[i]
                    previous_bit = previous_pref_bits[i]
                    bit = 0 
                    if pref_bit == 1:
                        bit = 1 - previous_bit
                    else:
                        bit = previous_bit 
                    element += bit * (2 ** base)
                    base += 1
                
                result.append(element)
                previous_pref_bits = pref_bits
            
        return result 

if __name__ == '__main__':
    sol = Solution()
    pref = [0, 0, 0]
    result = sol.findArray(pref)
    print(result)

