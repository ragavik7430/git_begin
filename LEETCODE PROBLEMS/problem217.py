class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) != len(set(nums)):
            return True
        else:
            return False
        
#Example 1:
#Input: nums = [1,2,3,1]
#Output: true