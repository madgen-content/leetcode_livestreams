# VERSION 1 ------------------------------------------
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        baseCosts.sort()
        toppingCosts.sort()

        self.best_diff = float('inf')
        for b in baseCosts:
            self.optimized_explore_topping(b, toppingCosts, target)

        return target - self.best_diff
    
    def optimized_explore_topping(self, base, toppings, target):
        d  = target - base
        if abs(d) <= abs(self.best_diff):
            if abs(d) < abs(self.best_diff) or base < target:
                self.best_diff = d
        elif base > target:
            return

        for i in range(len(toppings)):
            self.optimized_explore_topping(base, toppings[i+1:], target)
            self.optimized_explore_topping(base + toppings[i], toppings[i+1:], target)
            self.optimized_explore_topping(base + 2*toppings[i], toppings[i+1:], target)
        return

# VERSION 2 ------------------------------------------
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        baseCosts.sort()
        toppingCosts.sort()

        self.best_diff = float('inf')
        for b in baseCosts:
            self.optimized_explore_topping(b, toppingCosts, target, 0)

        return target - self.best_diff
    
    def optimized_explore_topping(self, base, toppings, target, i):
        d  = target - base
        if abs(d) <= abs(self.best_diff):
            if abs(d) < abs(self.best_diff) or base < target:
                self.best_diff = d
        elif base > target:
            return

        for i in range(i, len(toppings)):
            self.optimized_explore_topping(base, toppings, target, i+1)
            self.optimized_explore_topping(base + toppings[i], toppings, target, i+1)
            self.optimized_explore_topping(base + 2*toppings[i], toppings, target, i+1)
        return