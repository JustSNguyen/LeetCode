from collections import defaultdict

class Solution:
    def sortVowels(self, s: str) -> str:
        vowels_count = defaultdict(int)
        vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
        vowels_dict = {vowel: 1 for vowel in vowels}

        for char in s:
            if char in vowels_dict:
                vowels_count[char] += 1

        sorted_vowels_in_s = []
        for vowel in vowels:
            sorted_vowels_in_s.extend([vowel for _ in range(vowels_count[vowel])])

        result = []
        j = 0
        for char in s:
            if char in vowels_dict:
                result.append(sorted_vowels_in_s[j])
                j += 1
            else:
                result.append(char)

        return ''.join(result)

if __name__ == '__main__':
    sol = Solution()
    s = "lYmpH"
    result = sol.sortVowels(s)
    print(result)
