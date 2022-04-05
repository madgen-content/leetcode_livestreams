class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        while arr:
            found = False
            for i, parr in enumerate(pieces):
                if parr == arr[0:len(parr)]:
                    arr = arr[len(parr)::]
                    found = True
                    del pieces[i]
                    break
            if found == False:
                return False
        return True

