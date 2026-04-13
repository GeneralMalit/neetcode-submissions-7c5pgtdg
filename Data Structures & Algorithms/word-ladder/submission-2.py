class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        front, back = {beginWord}, {endWord}
        if endWord not in wordSet:
            return 0
        steps = 1

        while front:
            new_front = set()
            if len(front) > len(back):
                front, back = back, front
            for word in front:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word in back:
                            return steps + 1
                        if new_word in wordSet:
                            new_front.add(new_word)
                            wordSet.remove(new_word)
            front = new_front
            steps += 1
        return 0
