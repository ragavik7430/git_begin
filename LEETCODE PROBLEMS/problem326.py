class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if  n<=0:
            return False
        while (n!=1):
            r=n%3
            if(r!=0):
                 return False
            n//=3
        return True
#Example 1:
#Input: n = 27
#Output: true
