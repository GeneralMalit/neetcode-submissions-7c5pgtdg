class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True


    def search(self, word: str) -> bool:
        def dfs(node, idx):
            if idx == len(word):
                return node.word
                
            char = word[idx]

            if char == ".":
                for children in node.children:
                    if dfs(node.children[children], idx + 1):
                        return True
 
                return False
            else:
                if char not in node.children:
                    return False
                else:
                    return dfs(node.children[char], idx + 1)


        return dfs(self.root, 0)
