from typing import List 

class Node:
    def __init__(self):
        self.children = dict()

    def __contains__(self, word):
        cur = self 
        for char in word:
            if char not in cur.children:
                return False 
            
            cur = cur.children[char]
        
        return True 

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(i, j, visited, parent):
            char = board[i][j]
            if char not in parent.children:
                parent.children[char] = Node()
            
            visited[i][j] = True 

            offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for offset in offsets:
                ni, nj = i + offset[0], j + offset[1]
                if ni < 0 or nj < 0 or ni == M or nj == N or visited[ni][nj]:
                    continue 
                    
                dfs(ni, nj, visited, parent.children[char])
            
            visited[i][j] = False 

        M = len(board)
        N = len(board[0])
        root = Node()
        for i in range(M):
            for j in range(N):
                visited = [[False for _ in range(N)] for _ in range(M)]
                dfs(i, j, visited, root)
        
        result = []
        for word in words:
            if word in root:
                result.append(word)
        
        return result 

