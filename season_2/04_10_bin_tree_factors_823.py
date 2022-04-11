class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return len(arr)

        mem = {}
        arr = sorted(arr)
        for i, n in enumerate(arr):
            mem[i] = 1
        
        for i, n in enumerate(arr):
            for dec in range(i):
                j = i - 1 - dec 
                f1 = arr[j]
                f2, rem = divmod(n, f1)
                if rem == 0 and f2 in arr[:j+1]:
                    k = arr.index(f2)
                    order_mul = 1 if f1 == f2 else 2
                    mem[i] += mem[j] * mem[k] * order_mul
        
        return sum(mem.values()) % 1_000_000_007

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return len(arr)
        
        arr.sort()
        mem = {}
        for n in arr: mem[n] = 1
        
        for i, n in enumerate(arr):
            for dec in range(i):
                j = i - 1 - dec 
                f1 = arr[j]
                f2, rem = divmod(n, f1)
                if rem == 0 and f2 in mem:
                    k = arr.index(f2)
                    if k <= j:
                        order_mul = 1 if f1 == f2 else 2
                        mem[n] += mem[f1] * mem[f2] * order_mul
        
        return sum(mem.values()) % 1_000_000_007