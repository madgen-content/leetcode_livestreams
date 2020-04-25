class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        replacements = zip(indexes, sources, targets)
        good_replacements = [r for r in replacements if S[r[0]:r[0]+len(r[1])] == r[1]]
        good_replacements.sort(key = lambda x: x[0])
        built_str = []
        i = 0
        j = 0
        while i < len (S):
            if j < len(good_replacements):
                rep = good_replacements[j]
                if i == rep[0]:
                    built_str.append(rep[2])
                    i += len(rep[1])
                    j += 1
                else:
                    built_str.append(S[i])
                    i += 1
            else:
                built_str.append(S[i:])
                break
        return ''.join(built_str)

# zombiekillerwhale
class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        res = ''
        indexes, sources, targets = zip(*sorted(zip(indexes, sources, targets), key=lambda x: x[0]))
        i = 0
        r_idx = 0
        while i < len(S):
            if r_idx < len(indexes) and i == indexes[r_idx]:
                src = sources[r_idx]
                target = targets[r_idx]
                if S[i:i+len(src)] == src:
                    res += target
                    i += len(src)
                r_idx += 1
                continue
            res += S[i]
            i += 1
        return res