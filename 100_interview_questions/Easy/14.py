from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def get_common_prefix(str1: str, str2: str) -> int:
            N1 = len(str1)
            N2 = len(str2)
            prefix_length = 0
            for i in range(N1):
                if i >= N2 or str1[i] != str2[i]:
                    break 

                prefix_length += 1 
            
            return str1[:prefix_length]

        prefix_length = 10**6
        for string in strs:
            prefix_length = min(prefix_length, len(get_common_prefix(strs[0], string)))
        
        return strs[0][:prefix_length]



