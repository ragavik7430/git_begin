class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        p=0
        n=0
        for i in nums:
            if i > 0:
                p+=1
            elif i<0:
                n+=1
        return max(p,n)
#Example 1:
#Input: nums = [-2,-1,-1,1,2,3]
#Output: 3