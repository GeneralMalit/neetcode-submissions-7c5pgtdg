from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)

        res = []

        def visit(airport):
            while graph[airport]:
                place = graph[airport].pop()
                visit(place)
            res.append(airport)
        visit("JFK")
        return res[::-1]