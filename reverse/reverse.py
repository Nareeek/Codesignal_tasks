class Solution:
    def reverse(self, x: int) -> int:
        if len(str(x)) > 11 or x == 0:
            return 0
        
        t, x = x, abs(x)
        
        a = ""
        while x > 0:
            a += str(x % 10)
            x //= 10
        
        a = -int(a) if t < 0 else int(a) 
        
        return a if -2147483648 <= a < 2147483648 else 0