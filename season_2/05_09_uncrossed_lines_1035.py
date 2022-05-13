from typing import *
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m,n = len(nums1), len(nums2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                c1 = nums1[i-1]
                c2 = nums2[j-1]
                
                possible = [dp[i-1][j],dp[i][j-1]]
                if c1 == c2:
                    possible.append(dp[i-1][j-1]+1)
                
                dp[i][j] = max(possible)
        
        return dp[-1][-1]