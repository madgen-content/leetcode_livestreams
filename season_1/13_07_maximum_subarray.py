class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = float('-inf')
        current = 0
        nxt = 0
        for n in nums:
            nxt = current + n
            if nxt >= 0:
                current = nxt
            else:
                current = 0
            
            if nxt > best:
                best = nxt
        
        return best

# recursive soln?
# https://leetcode.com/problems/maximum-subarray/discuss/20200/Share-my-solutions-both-greedy-and-divide-and-conquer