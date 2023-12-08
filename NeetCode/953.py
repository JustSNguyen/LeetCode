from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        position = dict()
        position[""] = -1
        for i, char in enumerate(order):
            position[char] = i

        for i in range(1, len(words)):
            prev_word = words[i - 1]
            cur_word = words[i]
            j1 = 0
            j2 = 0

            while j1 < len(prev_word) or j2 < len(cur_word):
                prev_char = prev_word[j1] if j1 < len(prev_word) else ""
                cur_char = cur_word[j2] if j2 < len(cur_word) else ""

                if position[prev_char] < position[cur_char]:
                    break

                if position[prev_char] == position[cur_char]:
                    j1 += 1
                    j2 += 1
                    continue

                return False

        return True

if __name__ == '__main__':
    sol = Solution()
    words = ["zirqhpfscx","zrmvtxgelh","vokopzrtc","nugfyso","rzdmvyf","vhvqzkfqis","dvbkppw","ttfwryy","dodpbbkp","akycwwcdog"]
    order = "khjzlicrmunogwbpqdetasyfvx"
    result = sol.isAlienSorted(words, order)
    print(result)