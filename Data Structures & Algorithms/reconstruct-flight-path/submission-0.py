class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
        route = []

        def visit(airport):
            while graph[airport]:
                travel = graph[airport].pop()
                visit(travel)
            route.append(airport)
        
        visit("JFK")
        return route[::-1]