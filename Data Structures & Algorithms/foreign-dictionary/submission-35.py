from collections import defaultdict, deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        in_degree = {c:0 for word in words for c in word}
        adj = defaultdict(set)
        n = len(words)
        for i in range(n - 1):
            w1, w2 = words[i], words[i + 1]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break
        
        res = []
        q = deque([i for i in in_degree if in_degree[i] == 0])

        while q:
            curr = q.popleft()
            res.append(curr)
            for nei in adj[curr]:
                in_degree[nei] -=1
                if in_degree[nei] == 0:
                    q.append(nei)
        
        return "".join(res) if max(in_degree.values()) == 0 else ""