class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {}

        for i in range(len(S)):
            c = S[i]
            last[c] = i
        

        part_lens = []
        end = 0
        for i in range(len(S)):
            c = S[i]
            end = max(end, last[c])
            if end == i:
                app = end - sum(part_lens) + 1
                part_lens.append(app)
        
        return part_lens

# ==================
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        endpts = {}
        for i in range(len(S)):
            c = S[i]
            endpts[c]=i
        
        ans = []
        start = 0
        i = 0
        j = 0
        while i < len(S):
            j = max(j, endpts[S[i]])
            
            if i == j:
                ans.append(j-start+1)
                start = i+1
            i+= 1
        
        return ans