class Solution:
    def reverse(self, x: int) -> int:
        
        si = -1 if x < 0 else 1
        s=0
        x=abs(x)
        while(x>0):
            r=x%10
            s=s*10+r
            x//=10
        if s < -(2**31) or s > 2**31 - 1:
            return 0
        return s*si
#Example 1:
#Input: x = 123
#Output: 321