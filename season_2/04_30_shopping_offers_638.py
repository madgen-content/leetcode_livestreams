from typing import *
from functools import lru_cache

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        self.price = price
        self.special = special
        needs = tuple(needs)
        self.memo = {}
        return self.solve_remainder(needs)
    
    def solve_remainder(self, needs):
        if needs not in self.memo:
            # this combo hasn't been analyzed before, compute baseline
            best = sum(self.price[i]*n for i,n in enumerate(needs))
            max_uses = self.calc_specials_max_usage(needs)

            for spec_i,special in enumerate(self.special):
                for n in range(1,max_uses[spec_i]+1):
                    # get the cost basis of the offer * n
                    special_cost = special[-1]*n

                    # subtract offer items from needs for new needs
                    rneeds = tuple( need-(special[i]*n) for i,need in enumerate(needs))

                    # calculate baseline and replace if better
                    baseline = sum(self.price[i]*n for i,n in enumerate(rneeds))
                    simple_tot = baseline + special_cost
                    if simple_tot < best:
                        best = simple_tot

                    # recursively consider all other offers with only n applications of this offer, get best
                    better_cost = self.solve_remainder(rneeds)
                    better_tot = better_cost + special_cost

                    if better_tot < best:
                        best = better_tot
            self.memo[needs] = best
        
        return self.memo[needs]

    @lru_cache
    def calc_specials_max_usage(self, needs):
        special_maxes = []
        for s in self.special:
            lo = min(n // s[i] for i,n in enumerate(needs) if s[i] > 0)
            special_maxes.append(lo)
        return special_maxes

# =================================================================================
# this shitty brute force actually works just as well for some reason
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        self.price = price
        self.special = special
        needs = tuple(needs)
        return self.solve_remainder(needs)
    
    def solve_remainder(self, needs, max_special_index=-1):
        # this combo hasn't been analyzed before, compute baseline
        best = sum(self.price[i]*n for i,n in enumerate(needs))
        max_uses = self.calc_specials_max_usage(needs)

        for spec_i,special in enumerate(self.special):
            if spec_i <= max_special_index:
                continue
            for n in range(1,max_uses[spec_i]+1):
                # get the cost basis of the offer * n
                special_cost = special[-1]*n

                # subtract offer items from needs for new needs
                rneeds = tuple( need-(special[i]*n) for i,need in enumerate(needs))

                # calculate baseline and replace if better
                baseline = sum(self.price[i]*n for i,n in enumerate(rneeds))
                simple_tot = baseline + special_cost
                if simple_tot < best:
                    best = simple_tot

                # recursively consider all other offers with only n applications of this offer, get best
                better_cost = self.solve_remainder(rneeds, spec_i)
                better_tot = better_cost + special_cost

                if better_tot < best:
                    best = better_tot
        return best

    @lru_cache
    def calc_specials_max_usage(self, needs):
        special_maxes = []
        for s in self.special:
            lo = min(n // s[i] for i,n in enumerate(needs) if s[i] > 0)
            special_maxes.append(lo)
        return special_maxes