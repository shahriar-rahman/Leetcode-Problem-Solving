# Runtime 41ms
# Memory 16.39mb

class Solution:
    def reverse(self, x: int) -> int:
        res = 0

        sign = -1 if x < 0 else 1

        x *= sign

        while x > 0:
            mod = x % 10
            res = res * 10 + mod
            x //= 10

        if sign * res < -2**31 or sign * res > 2**31 - 1:
            return 0
        
        return res * sign