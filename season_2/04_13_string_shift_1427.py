class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        if s == "":
            return ""
        
        shift_total = sum([(1 if dir==0 else -1)*size for dir, size in shift])

        if shift_total == 0:
            return s
        else:
            shift_total %= len(s)
            return s[shift_total:] + s[:shift_total]