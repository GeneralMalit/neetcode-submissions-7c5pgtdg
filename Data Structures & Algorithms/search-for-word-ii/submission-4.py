class TrieNode:
    def __init__(self):
        self.word = None
        self.children = {}


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = word
        rows, cols = len(board), len(board[0])
        res, visited = [], set()

        def dfs(r, c, node):
            if (r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or board[r][c] not in node.children):
                return
            
            visited.add((r, c))
            curr_char = board[r][c]
            next_node = node.children[curr_char]

            if next_node.word:
                res.append(next_node.word)
                next_node.word = None
            
            dfs(r - 1, c, next_node)
            dfs(r + 1, c, next_node)
            dfs(r, c - 1, next_node)
            dfs(r, c + 1, next_node)

            visited.remove((r, c))

            if not next_node.children:
                del node.children[curr_char]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        
        return res