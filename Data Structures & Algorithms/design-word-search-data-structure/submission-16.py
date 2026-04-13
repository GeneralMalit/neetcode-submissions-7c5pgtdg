class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

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
        def dfs(index, node):
            if index == len(word):
                return node.word
            
            char = word[index]

            if char == '.':
                for child in node.children:
                    if dfs(index + 1, node.children[child]):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(index + 1, node.children[char])
        return dfs(0, self.root)