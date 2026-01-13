class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        from collections import defaultdict
        
        if not roads:
            return 0
        
        # Build adjacency list
        graph = defaultdict(list)
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)
        
        self.fuel = 0
        
        def dfs(node, parent):
            # Returns number of people in subtree
            people = 1  # Current representative
            
            for neighbor in graph[node]:
                if neighbor != parent:
                    people += dfs(neighbor, node)
            
            # If not at capital, need to travel to parent
            if node != 0:
                # Number of cars needed = ceil(people / seats)
                cars = (people + seats - 1) // seats
                self.fuel += cars
            
            return people
        
        dfs(0, -1)
        return self.fuel