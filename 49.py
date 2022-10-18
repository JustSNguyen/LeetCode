from typing import List 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = list(map(lambda str: (''.join(sorted(str)), str), strs))
        exist = dict()

        for sorted_str, original_str in sorted_strs:
            if not sorted_str in exist:
                exist[sorted_str] = []

            exist[sorted_str].append(original_str)
        
        result = []
        for anagrams_list in exist.values():
            result.append(anagrams_list)

        return result 

if __name__ == '__main__':
    sol = Solution()
    strs = ["", ""]
    print(sol.groupAnagrams(strs))