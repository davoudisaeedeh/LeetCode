class Solution:
    def climbStairs(self, n: int) -> int:
        f, s = 1, 2
        for _ in range(2, n+1):
            f, s = s, f+s
        return f
        