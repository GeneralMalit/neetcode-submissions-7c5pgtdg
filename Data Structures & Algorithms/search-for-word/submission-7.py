from collections import Counter
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        board_ct = Counter([i for row in board for i in row])
        word_ct = Counter(word)

        for i, val in word_ct.items():
            if board_ct[i] < val:
                return False
            
        if board_ct[word[0]] < board_ct[word[-1]]:
            word = word[::-1]

        def dfs(r, c, i):
            if i == len(word):
                return True

            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False
            
            temp = board[r][c]
            board[r][c] = "#"

            if dfs(r - 1, c, i + 1) or dfs(r + 1, c, i + 1) or dfs(r, c - 1, i + 1) or dfs(r, c + 1, i + 1):
                return True
            board[r][c] = temp 
        
        for r in range(rows):
            for c in range(cols):
                if word[0] == board[r][c] and dfs(r, c, 0):
                    return True

        return False 