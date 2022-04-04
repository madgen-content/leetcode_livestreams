class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        if K >= len(A):
            return len(A)
        
        if len(A) == 0:
            return 0

        listsum = sum(A)
        
        if listsum == len(A):
            return len(A)

        if listsum == 0:
            return 0 
        
        i = 0
        j = 0
        max_width = 0
        max_flips = K
        
        if A[0] == 0 and max_flips > 0:
            K -=1
        
        while True:
            # justify j with i in degenerate case
            j = max(i, j)

            # move j forward until flips run out
            while K > 0 and j < len(A)-1:
                if A[j+1] == 0:
                    K -= 1
                j += 1
                if j == len(A) - 1:
                    break
            
            # move j through 1's
            while j < len(A) - 1 and A[j+1] == 1 and (max_flips > 0 or A[j] == 1):
                j += 1

            # calculate width
            max_width = max(max_width, j - i + 1)

            # move i forward until a flip is recovered
            while A[i] == 1 and i < j:
                i += 1
            i += 1

            # only increment flips if one can be recovered
            if max_flips > 0:
                K += 1

            if j == len(A) - 1:
                break
        return max_width