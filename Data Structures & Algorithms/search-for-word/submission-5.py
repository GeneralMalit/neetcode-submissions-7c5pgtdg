from collections import Counter
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        board_ct = Counter(char for row in board for char in row)
        word_ct = Counter(word)

        for ch, count in word_ct.items():
            if board_ct[ch] < count:
                return False

        if board_ct[word[:-1]] > board_ct[word[0]]:
            word = word[::-1]
        ROWS, COLS = len(board), len(board[0])
        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != word[i]:
                return False
            temp = board[r][c]
            board[r][c] = "#"
            
            if dfs(r - 1, c, i + 1) or dfs(r + 1, c, i + 1) or dfs(r, c - 1, i + 1) or dfs(r, c + 1, i + 1):
                return True
            
            board[r][c] = temp

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False