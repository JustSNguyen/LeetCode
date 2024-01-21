from typing import List 
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strings: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for string in strings:
            sorted_str = str(sorted(string))
            anagrams[sorted_str].append(string)
        
        return [group for group in anagrams.values()]