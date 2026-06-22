class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            if len(str(i)) % 2==0:
                c+=1
        return c
#Example 1:
#Input: nums = [12,345,2,6,7896]
#Output: 2