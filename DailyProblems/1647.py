from collections import defaultdict


class Solution:
    def minDeletions(self, s: str) -> int:
        character_frequency = defaultdict(int)

        for char in s:
            character_frequency[char] += 1 

        character_with_frequency = dict()
        max_frequency = 0
        need_to_delete_chars_original_frequency = []
        for char, frequency in character_frequency.items():
            max_frequency = max(frequency, max_frequency)

            if frequency not in character_with_frequency:
                character_with_frequency[frequency] = char 
            else:
                need_to_delete_chars_original_frequency.append(frequency)
        
        sorted_need_to_delete_chars_original_frequency = list(sorted(need_to_delete_chars_original_frequency))
        total_deletions = 0
        for possible_frequency in range(max_frequency, 0, -1):
            if possible_frequency in character_with_frequency:
                continue
            
            if not sorted_need_to_delete_chars_original_frequency:
                break 

            original_frequency = sorted_need_to_delete_chars_original_frequency[-1]
            if possible_frequency < original_frequency:
                total_deletions += original_frequency - possible_frequency 
                sorted_need_to_delete_chars_original_frequency.pop()
        
        total_deletions += sum(sorted_need_to_delete_chars_original_frequency)
        return total_deletions
        
if __name__ == '__main__':
    sol = Solution()
    string = "bogoidmdkbllehemdkfofcieckdoffiokflejeeffhihfbbfffboklaoochielobmcekaeoajicke"
    print(sol.minDeletions(string))