class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            
            if index == len(word):
                return node.word
            c = word[index]
            if c == ".":
                for child in node.children:
                    if dfs(index + 1, node.children[child]):
                        return True
                return False
            else:
                if c not in node.children:
                    return False
                return dfs(index + 1, node.children[c])
        return dfs(0, self.root)
            
            

