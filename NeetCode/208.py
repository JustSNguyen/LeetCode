class TrieNode:
    def __init__(self, value, is_end_of_word):
        self.value = value
        self.is_end_of_word = is_end_of_word
        self.children = dict()

class Trie:
    def __init__(self):
        self.root = TrieNode("", False)

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode(char, False)

            cur = cur.children[char]

        cur.is_end_of_word = True

    def search(self, word: str) -> bool:
        cur = self.root

        for char in word:
            if char not in cur.children:
                return False

            cur = cur.children[char]

        return cur.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for char in prefix:
            if char not in cur.children:
                return False

            cur = cur.children[char]

        return True