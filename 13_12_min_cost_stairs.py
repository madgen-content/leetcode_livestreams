class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n_dp_entries = len(cost) + 1

        min_costs = []
        for i in range(n_dp_entries):
            if i <= 1:
                min_costs.append(0)
            else:
                c1 = min_costs[i-1] + cost[i-1]
                c2 = min_costs[i-2] + cost[i-2]
                min_costs.append(min( c1, c2))

        return min_costs[-1]