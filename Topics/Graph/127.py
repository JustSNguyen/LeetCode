from typing import List
from collections import deque

class Solution:
    def ladderLength(self, begin: str, end: str, words: List[str]) -> int:
        words = set(words)
        q = deque()
        q.append(begin)

        length = 1
        while q:
            N = len(q)

            for i in range(N):
                cur_word = q.popleft()

                if cur_word == end:
                    return length

                for j in range(len(cur_word)):
                    for ascii in range(ord('a'), ord('z') + 1):
                        new_word = cur_word[:j] + chr(ascii) + cur_word[j + 1:]
                        if new_word not in words:
                            continue

                        words.remove(new_word)
                        q.append(new_word)

            length += 1

        return 0

if __name__ == '__main__':
    sol = Solution()
    begin = "hit"
    end = "cog"
    words = ["hot","dot","dog","lot","log","cog"]
    result = sol.ladderLength(begin, end, words)
    print(result)
