from collections import defaultdict


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        char_count = defaultdict(int)
        existed = set()

        for char in s:
            char_count[char] += 1

        stack = []

        for char in s:
            if char in existed:
                char_count[char] -= 1
                continue

            while stack and char < stack[-1] and char_count[stack[-1]] > 0:
                existed.remove(stack.pop())

            stack.append(char)
            existed.add(char)
            char_count[char] -= 1

        return "".join(stack)

if __name__ == '__main__':
    sol = Solution()
    test = "bbcaac"
    result = sol.removeDuplicateLetters(test)
    print(result)
