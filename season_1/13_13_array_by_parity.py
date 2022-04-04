def exchange(arr, p1, p2):
    arr[p1] = arr[p1] + arr[p2]
    arr[p2] = arr[p1] - arr[p2]
    arr[p1] = arr[p1] - arr[p2]
    return
    
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even_off_runner = 0
        odd_off_runner  = 1

        while even_off_runner < len(A) and odd_off_runner < len(A):
            while even_off_runner < len(A):
                if A[even_off_runner] % 2 == 1:
                    break
                even_off_runner += 2
            
            while odd_off_runner < len(A):
                if A[odd_off_runner] % 2 == 0:
                    break
                odd_off_runner += 2
            
            if even_off_runner < len(A) and odd_off_runner < len(A):
                exchange(A, even_off_runner, odd_off_runner)
                even_off_runner += 2
                odd_off_runner  += 2

        return A
    
# alternative
# dumber, but faster
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odds = []
        evens = []

        for n in A:
            if n % 2 == 0:
                evens.append(n)
            else:
                odds.append(n)
        
        ret = []
        for i in range(len(A)):
            if i % 2 == 0:
                ret.append(evens.pop())
            else:
                ret.append(odds.pop())

        return ret

# better two-pointer framing
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        
        size = len(A)
        
        sorted_array = [0]*size
        
        # two pointers for even numbers, as well as odd numbers, respectively.
        even_index, odd_index = 0, 1
        
        for x in A:
            
            if x & 1:
                # odd numbers
                sorted_array[odd_index] = x
                odd_index += 2
            else:
                # even numbers
                sorted_array[even_index] = x
                even_index += 2
                
        return sorted_array