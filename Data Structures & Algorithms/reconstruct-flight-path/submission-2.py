from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for u, v in sorted(tickets, reverse=True):
            graph[u].append(v)
        
        res = []
        def visit(place):
            while graph[place]:
                airport = graph[place].pop()
                visit(airport)
            res.append(place)
        
        visit("JFK")
        return res[::-1]