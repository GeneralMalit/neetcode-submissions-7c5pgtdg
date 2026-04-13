class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.word = True
        

    def search(self, word: str) -> bool:
        def dfs(idx, node):
            if idx == len(word):
                return node.word
            char = word[idx]
            if char == ".":
                for child in node.children:
                    if dfs(idx + 1, node.children[child]):
                        return True
                return False 
            else:
                if char not in node.children:
                    return False
                return dfs(idx + 1, node.children[char])
        return dfs(0, self.root)        
