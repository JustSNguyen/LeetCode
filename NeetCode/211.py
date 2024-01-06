class Node:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False 

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root 
        for char in word:
            if char not in cur.children:
                cur.children[char] = Node()
            
            cur = cur.children[char]
        
        cur.is_end_of_word = True 

    def search(self, word: str) -> bool:
        return self.search_starts_from(self.root, 0, word)
    
    def search_starts_from(self, node, char_index, word):
        if char_index == len(word):
            return node.is_end_of_word

        char = word[char_index]
        if char != ".":
            if char not in node.children:
               return False 
            else: 
                return self.search_starts_from(node.children[char], char_index + 1, word)
        
        for char in node.children:
            if self.search_starts_from(node.children[char], char_index + 1, word):
                return True 
        
        return False 

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)