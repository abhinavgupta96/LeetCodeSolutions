class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Sort by the cost difference of flying to City A vs City B
        costs.sort(key=lambda x: x[0] - x[1])
        
        total_cost = 0
        n = len(costs) // 2
        
        # First n people to City A, next n people to City B
        for i in range(n):
            total_cost += costs[i][0]  # Cost for City A
        for i in range(n, 2 * n):
            total_cost += costs[i][1]  # Cost for City B
        
        return total_cost
