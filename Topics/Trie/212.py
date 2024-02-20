from typing import List


class TrieNode:
    def __init__(self):
        self.children = dict()

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def search(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False

            cur = cur.children[char]

        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        trie = Trie()
        visited = [[False for _ in range(n)] for _ in range(m)]
        def dfs(i, j, parent):
            offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for offset in offsets:
                ni, nj = i + offset[0], j + offset[1]
                if i < 0 or j < 0 or i == m or j == n or visited[i][j]:
                    continue
                visited[ni][nj] = True
                char = board[ni][nj]
                new_parent = TrieNode()
                parent.children[char] = new_parent
                dfs(ni, nj, new_parent)
                visited[ni][nj] = False

        start_node = TrieNode()
        trie.root.children[board[0][0]] = start_node

        result = []
        for word in words:
            if word[0] not in trie.root.children:
                for i in range(m):
                    for j in range(n):
                        if board[i][j] == word[0]:
                            if word[0] not in trie.root.children:
                                trie.root.children[word[0]] = TrieNode()

            elif trie.search(word):



            if trie.search(word):
                result.append(word)

        return result