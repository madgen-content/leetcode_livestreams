class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def memoize(f):
            cache = {}
            def helper(nums, bounds):
                if bounds not in cache:
                    cache[bounds] = f(nums, bounds)
                return cache[bounds]
            return helper

        @memoize
        def opt_score_delta(nums, bounds):
            i,j = bounds
            moves = i + (len(nums) - 1 - j)
            player = moves % 2
            coef = (-1) ** player
            opt_fn = [max, min][player]

            if i == j:
                return coef * nums[i]
            
            return opt_fn(coef * nums[i] + opt_score_delta(nums, (i+1, j)), coef * nums[j] + opt_score_delta(nums, (i, j-1)))

        final_score = opt_score_delta(nums, (0, len(nums)-1))
        return final_score >= 0