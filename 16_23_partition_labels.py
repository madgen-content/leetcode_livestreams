class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {}

        for i in range(len(S)):
            c = S[i]
            last[c] = i
        

        part_lens = []
        right = 0
        end = 0
        for i in range(len(S)):
            c = S[i]
            end = max(end, last[c])
            if end == i:
                app = end - sum(part_lens) + 1
                part_lens.append(app)
        
        return part_lens