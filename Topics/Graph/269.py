from collections import defaultdict, deque

class Solution:
    def alienDictionary(self, words):
        N = len(words)
        adj = defaultdict(set)
        all_chars = set()

        for word in words:
            for char in word:
                all_chars.add(char)

        for i in range(N - 1):
            j = i + 1
            min_length = min(len(words[i]), len(words[j]))
            for k in range(min_length):
                if words[i][k] != words[j][k]:
                    adj[words[i][k]].add(words[j][k])
                    break

        WHITE = 0
        GREY = 1
        BLACK = 2

        colors = defaultdict(lambda: WHITE)
        orders = deque()

        def dfs(node):
            if colors[node] == GREY:
                raise Exception("Cycle")

            if colors[node] == BLACK:
                return

            colors[node] = GREY
            for neighbor in adj[node]:
                dfs(neighbor)

            colors[node] = BLACK
            orders.appendleft(node)

        for char in all_chars:
            try:
                dfs(char)
            except:
                return ""

        return ''.join(orders)

if __name__ == '__main__':
    sol = Solution()
    test = [
        "zabcde",
        "xab",
    ]
    result = sol.alienDictionary(test)
    print(result)


