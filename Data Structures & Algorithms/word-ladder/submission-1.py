class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        front = {beginWord}
        back = {endWord}

        if endWord not in wordSet:
            return 0

        steps = 1
        while front:
            if len(front) > len(back):
                front, back = back, front
            
            next_front = set()

            for word in front:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word in back:
                            return steps + 1
                        
                        if new_word in wordSet:
                            next_front.add(new_word)
                            wordSet.remove(new_word)
            
            front = next_front
            steps += 1
        return 0