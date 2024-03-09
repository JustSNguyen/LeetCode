class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()

            cur = cur.children[char]

        cur.is_end_of_word = True

    def search(self, word: str) -> bool:
        self.word = word
        return self.search_from(self.root, 0)

    def search_from(self, start, i):
        char = self.word[i]
        if i == len(self.word) - 1:
            if char != ".":
                return char in start.children and start.children[char].is_end_of_word

            for char in start.children:
                if start.children[char].is_end_of_word:
                    return True

            return False

        if char != ".":
            if char not in start.children:
                return False

            return self.search_from(start.children[char], i + 1)

        for child in start.children:
            if self.search_from(start.children[child], i + 1):
                return True

        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)