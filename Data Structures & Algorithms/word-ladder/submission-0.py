class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        front = {beginWord}
        back = {endWord}
        count = 1

        while front:
            if len(front) > len(back):
                front, back = back, front
            
            next_front = set()

            for word in front:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word in back:
                            return count + 1
                        if new_word in wordSet:
                            next_front.add(new_word)
                            wordSet.remove(new_word)
            
            count += 1
            front = next_front
    
        return 0