def rec_get_sum_solns(target, soln_set, current_soln, candidates):
    if sum(current_soln) == target:
        soln_set.add(tuple(current_soln))
    
    upcoming_candidates = candidates[:]
    for n in candidates:
        next_soln = current_soln + [n]
        upcoming_candidates.remove(n)
        if sum(next_soln) < target:
            rec_get_sum_solns(target, soln_set, next_soln, upcoming_candidates)
        elif sum(next_soln) == target:
            soln_set.add(tuple(next_soln))
        else:
            return
    return

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        soln_set = set()
        candidates.sort()
        candidates = [x for x in candidates if x <= target]
        rec_get_sum_solns(target, soln_set, [], candidates)
        return soln_set