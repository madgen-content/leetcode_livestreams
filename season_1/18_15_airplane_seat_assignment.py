class Solution(object):
    def nthPersonGetsNthSeat(self, n):
        return (1 if n == 1 else 0.5)

# https://leetcode.com/problems/airplane-seat-assignment-probability/discuss/665271/short-proof-by-induction-for-P(n)-12-for-n-greater-1
# https://leetcode.com/problems/airplane-seat-assignment-probability/discuss/669454/Python-Simple-DP-solution-with-explanation